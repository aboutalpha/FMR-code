import numpy as np
import gurobipy as gp
from gurobipy import GRB
from repliclust import set_seed, Archetype, DataGenerator
import matplotlib.pyplot as plt
from tqdm import tqdm
from datetime import datetime


def master_optimize(model, m, n, l, Z, slack, slack_var):
    # Solve the problem
    model.optimize()

    # print("Display")
    # print(model.display())

    # Print objective value
    # print("Objective:", model.objVal)

    # Print variable values
    # for i, var in enumerate(model.getVars()):
    # print(f"{var.varName} = {var.x}")

    # Print dual variables
    # print("Dual values:")
    # for constr in model.getConstrs():
    # print(f"{constr.ConstrName}: {constr.Pi}")

    constraints = list(model.getConstrs())

    mu = [cons_i.Pi for cons_i in constraints[:n]]

    lmd = [cons_g.Pi for cons_g in constraints[n: n + l]]

    delta = constraints[n + l].Pi

    optimal_values_Z = [(Z[k].x) for k in range(m)]

    optimal_slack = []
    optimal_slack_sum = -1
    if slack:
        optimal_slack = [(slack_var[k].x) for k in range(n+l)]
        optimal_slack_sum = sum(optimal_slack)

    return model, mu, lmd, model.objVal, optimal_values_Z, delta, Z, slack_var, optimal_slack, optimal_slack_sum


def master_warm_start(model, Z, m, n, l, warm_start_new_columns, slack=(20,100,False), slack_var=None):
    print("Master Warm Start")
    print("warm_start_new_columns", warm_start_new_columns)
    model.reset(1)
    
    sol_size = len(warm_start_new_columns)
    for solNum, sol in enumerate(warm_start_new_columns):
        (cluster, new_t, new_r, (xc, yc), bound, objVal) = sol
        constrs = model.getConstrs()
        optimal_values_s = cluster + new_t + [1]
        print("optimal_values_s", optimal_values_s)
        new_z = model.addVar(vtype=GRB.CONTINUOUS, name="Z["+str(
            m-sol_size+solNum)+"]", column=gp.Column(optimal_values_s, constrs[:n+l+1]), obj=new_r)
        Z += [new_z]
    return master_optimize(model, m, n, l, Z, slack, slack_var)


def solve_master_problem_gurobi(n, m, l, r, s, t, beta, K, slack=(20,100,False)):
    # Create a Gurobi model
    model = gp.Model("MasterProblem")
    #model.Params.TimeLimit = 5
    #model.Params.LogToConsole = 0

    # Create decision variables
    Z = []
    for i in range(m):
        Z.append(model.addVar(vtype=GRB.CONTINUOUS, name="Z " + str(i)))
    # Z = model.addMVar(m, vtype=GRB.CONTINUOUS, name="Z")

    slack_var = [model.addVar(vtype=GRB.CONTINUOUS,
                              name="Slack " + str(i)) for i in range(n+l)]
    # Set objective function
    if slack[2] == False:
        model.setObjective(gp.quicksum(Z[i] * r[i]
                           for i in range(m)), GRB.MINIMIZE)
    else:
        model.setObjective(gp.quicksum(Z[i] * r[i] for i in range(m)) +
                           slack[0] * gp.quicksum(slack_var[i] for i in range(n)) + 
                           slack[1] * gp.quicksum(slack_var[i] for i in range(n,n+l)), GRB.MINIMIZE)

    # Constraints
    constraint1 = []
    constraint2 = []

    if slack[2] == False:
        for i in range(n):
            constraint1.append(
                model.addConstr(
                    gp.quicksum(s[k][i] * Z[k] for k in range(m)) == 1,
                    name="Constraint1_" + str(i),
                )
            )
    else:
        for i in range(n):
            constraint1.append(
                model.addConstr(
                    gp.quicksum(s[k][i] * Z[k]
                                for k in range(m)) + slack_var[i] == 1,
                    name="Constraint1_" + str(i),
                )
            )

    if slack[2] == False:
        for g in range(l):
            constraint2.append(
                model.addConstr(
                    gp.quicksum(t[g][k] * Z[k] for k in range(m)) >= beta[g],
                    name="Constraint2_" + str(g),
                )
            )
    else:
        for g in range(l):
            constraint2.append(
                model.addConstr(
                    gp.quicksum(t[g][k] * Z[k]
                                for k in range(m)) + slack_var[n+g] >= beta[g],
                    name="Constraint2_" + str(g),
                )
            )

    constraint_3 = [
        model.addConstr(gp.quicksum(Z[k]
                        for k in range(m)) == K, name="Constraint3")
    ]

    # for k in range(m):
    #     model.addConstr(Z[k] <= 1, name="Constraint4_"+str(k))
    #     model.addConstr(Z[k] >= 0, name="Constraint5_"+str(k))

    return master_optimize(model, m, n, l, Z, slack, slack_var)


def solve_master_problem_integer(n, m, l, r, s, t, beta, K):
    # Create a Gurobi model
    model = gp.Model("MasterProblemInteger")
    #model.Params.LogToConsole = 0

    # Create decision variables
    Z = model.addMVar(m, vtype=GRB.BINARY, name="Z")

    # Set objective function
    model.setObjective(gp.quicksum(Z[i] * r[i]
                       for i in range(m)), GRB.MINIMIZE)

    # Constraints
    constraint1 = []
    constraint2 = []

    for i in range(n):
        constraint1.append(
            model.addConstr(
                gp.quicksum(s[k][i] * Z[k] for k in range(m)) == 1,
                name="Constraint1_" + str(i),
            )
        )

    for g in range(l):
        constraint2.append(
            model.addConstr(
                gp.quicksum(t[g][k] * Z[k] for k in range(m)) >= beta[g],
                name="Constraint2_" + str(g),
            )
        )

    constraint_3 = [
        model.addConstr(gp.quicksum(Z[k]
                        for k in range(m)) == K, name="Constraint3")
    ]

    # Solve the problem
    model.optimize()

    # Print objective value
    # print("Objective:", model.objVal)

    # Print variable values
    # for i, var in enumerate(model.getVars()):
    #     print(f"{var.varName} = {var.x}")

    optimal_values_Z = [int(Z[k].x) for k in range(m)]

    return model.objVal, optimal_values_Z


def pricing_warm_start(model, r_var, mu, s_var, lmd, t_var, delta, n, l, cx_var, cy_var):
    objective = gp.quicksum(r_var[i] for i in range(n)) \
        - gp.quicksum(mu[i] * s_var[i] for i in range(n)) \
        - gp.quicksum(lmd[g] * t_var[g] for g in range(l)) \
        - delta
    model.setObjective(objective, GRB.MINIMIZE)
    model.reset(1)
    model.optimize()

    nSolutions = model.SolCount

    objectives = []
    pricing_new_columns = []

    for e in range(nSolutions):
        # print("Solution Number",e)
        model.setParam(GRB.Param.SolutionNumber, e)
        # print("Objective", model.PoolObjVal)
        objectives.append(model.PoolObjVal)
        # Print variable values
        # for var in model.getVars():
        #   print(f"{var.varName} = {var.Xn}")

        cluster = [int(np.round(s_var[i].Xn)) for i in range(n)]
        for i in range(n):
            if r_var[i].Xn == 0.16325638587582536:
                print("What is this", r_var[i], s_var[i], i)
        dist = [float(r_var[i].Xn) for i in range(n)]
        new_t = [int(np.round(t_var[g].Xn)) for g in range(l)]
        (xc, yc) = (cx_var.Xn, cy_var.Xn)
        bound = model.ObjBound
        objVal = model.PoolObjVal
        gap = np.abs(bound - objVal) / np.abs(objVal)
        pricing_new_columns.append((cluster, new_t, dist, (xc, yc), bound, objVal))
        
        #c0 = model.getConstrs()
        # for i in range(l,l+n):
        #     print(c0[i])
        #     print(c0[i].getAttr('ConstrName'))
        #     print(c0[i].getAttr('Sense'), c0[i].getAttr('RHS'), c0[i].getAttr('Slack'))
        
        #print("Obj Bound",bound)
        #print("Obj value", objVal)
        #print("Gap", gap)

    return objectives, pricing_new_columns


def solve_pricing_problem_gurobi(n, l, r, q, alpha, beta, delta, K, M, x, y, mu, lmd, lower, upper):
    # Create a Gurobi model
    model = gp.Model("PricingProblem")
    model.Params.PoolSearchMode = 2
    model.Params.PoolSolutions = 5
    model.Params.TimeLimit = 5
    model.Params.MIPGap = 0.1
    model.Params.LogToConsole = 0

    # Create decision variables
    r = model.addMVar(n, vtype=GRB.CONTINUOUS, name="R")
    s = model.addMVar(n, vtype=GRB.BINARY, name="S")
    t = model.addMVar(l, vtype=GRB.BINARY, name="t")
    cx = model.addVar(vtype=GRB.CONTINUOUS, lb=-100, name="cx")
    cy = model.addVar(vtype=GRB.CONTINUOUS, lb=-100, name="cy")

    # Objective function

    objective = gp.quicksum(r[i] for i in range(n)) \
        - gp.quicksum(mu[i] * s[i] for i in range(n)) \
        - gp.quicksum(lmd[g] * t[g] for g in range(l)) \
        - delta
    model.setObjective(objective, GRB.MINIMIZE)

    # Constraints
    constraints = []

    for g in range(l):
        constraints.append(model.addConstr(gp.quicksum(q[g][i] * s[i] for i in range(n)) + M*(
            1-t[g]) >= alpha * gp.quicksum(s[i] for i in range(n)), name="Constraint1"))

    for i in range(n):
        constraints.append(model.addConstr(
            r[i] + M*(1-s[i]) >= ((x[i] - cx)**2 + (y[i] - cy)**2), name="Constraint2"))
        constraints.append(model.addConstr(r[i] >= 0, name="Constraint3"))

    constraints.append(model.addConstr(gp.quicksum(
        s[i] for i in range(n)) >= lower, name="Constraint3"))
    constraints.append(model.addConstr(gp.quicksum(
        s[i] for i in range(n)) <= upper, name="Constraint4"))

    # Solve the problem
    model.optimize()
    
    
    nSolutions = model.SolCount

    objectives = []
    pricing_new_columns = []

    for e in range(nSolutions):
        # print("Solution Number",e)
        model.setParam(GRB.Param.SolutionNumber, e)
        # print("Objective", model.PoolObjVal)
        objectives.append(model.PoolObjVal)
        # Print variable values
        # for var in model.getVars():
        #   print(f"{var.varName} = {var.Xn}")

        cluster = [int(np.round(s[i].Xn)) for i in range(n)]
        for i in range(n):
            if r[i].Xn == 0.16325638587582536:
                print("What is this", r[i], s[i], i)
        dist = [float(r[i].Xn) for i in range(n)]
        new_t = [int(np.round(t[g].Xn)) for g in range(l)]
        (xc, yc) = (cx.Xn, cy.Xn)
        bound = model.ObjBound
        objVal = model.PoolObjVal
        gap = np.abs(bound - objVal) / np.abs(objVal)
        pricing_new_columns.append((cluster, new_t, dist, (xc, yc), bound, objVal))
        
        #c0 = model.getConstrs()
        # for i in range(l,l+n):
        #     print(c0[i])
        #     print(c0[i].getAttr('ConstrName'))
        #     print(c0[i].getAttr('Sense'), c0[i].getAttr('RHS'), c0[i].getAttr('Slack'))
        
        #print("Obj Bound",bound)
        #print("Obj value", objVal)
        #print("Gap", gap)
    

    # cluster = [int(np.round(s[i].x)) for i in range(n)]
    # dist = [float(r[i].x) for i in range(n)]
    # new_t = [int(np.round(t[g].x)) for g in range(l)]
    # (xc, yc) = (cx.x, cy.x)
    
    # bound = model.ObjBound
    # objVal = model.ObjVal
    
    # print("MIP Gap", model.MIPGap)
    # print("Obj Bound", bound)
    # print("Obj value", objVal)

    return model, r, s, t, cx, cy, objectives, pricing_new_columns


def t_value_correction(new_cluster, l, q, alpha, optimal_values_t):
    new_cluster_size = sum(new_cluster)
    new_cluster_arr = np.array(new_cluster)

    new_t = []
    for i in range(l):
        count = np.sum(new_cluster_arr & np.array(q[i]))
        if count >= alpha * new_cluster_size:
            new_t.append(1)
        else:
            new_t.append(0)
    return new_t

def write_model(master_model,file_name,counter,pricing_model):
    master_model.write("./model_write/" + file_name + "_master_out" + str(counter) + ".lp")
    master_model.write("./model_write/" + file_name + "_master_out" + str(counter) + ".sol")
    #pricing_model.write("./model_write/" + file_name + "_pricing_out" +str(counter) + ".mps")
    #pricing_model.write("./model_write/" + file_name + "_pricing_out" +str(counter) + ".mst")
    #pricing_model.write("./model_write/" + file_name + "_pricing_out" +str(counter) + ".sol")


def main_loop(file_name, iterations, K, n, m, l, r, beta, s, t, alpha, M, q, lower, upper, x, y, centers,slack):
    reduced_cost = 1
    counter = 0
    master_model = None
    pricing_model = None
    Z = None
    pbar = tqdm(total=iterations)
    objectives = []
    master_solutions = []
    repeat_check = []
    times = []
    slacks = []
    model_write_frequency = 100
    last_model_write = -model_write_frequency

    all_clusters = []
    for i in range(m):
        cluster = s[i]
        t_label = [j[i] for j in t]
        dist = r[i]
        (xc, yc) = centers[i]
        all_clusters.append((cluster, t_label, dist, (xc, yc), -1, -1))

    while counter < iterations:
        counter += 1
        pbar.update(1)
        print("Iteration #" + str(counter))
        time = datetime.now()
        times.append(time)
        print("Time", time)

        # Solve master problem
        if not master_model:
            master_model, mu, lmd, masterobj, optimal_values_Z, delta, Z, slack_var, optimal_slack, optimal_slack_sum = solve_master_problem_gurobi(
                n, m, l, r, s, t, beta, K, slack=slack)
            initial_obj = masterobj
        else:
            master_model, mu, lmd, masterobj, optimal_values_Z, delta, Z, slack_var, optimal_slack, optimal_slack_sum = master_warm_start(
                master_model, Z, m, n, l, warm_start_new_columns, slack, slack_var)
            

        objectives.append(masterobj)
        master_solutions.append(optimal_values_Z)
        slacks.append(optimal_slack)
        #print(counter, "Slack variables", optimal_slack)
        print(counter, "Sum of Slack Variables", optimal_slack_sum)
        print(counter, "Master Objective", masterobj)
        #print(counter, "Master Solution", optimal_values_Z)
        #print(counter, "Master Dual", mu)

        # Solve pricing problem
        if not pricing_model:
            pricing_model, r_var, s_var, t_var, cx_var, cy_var, reduced_cost, pricing_new_columns = solve_pricing_problem_gurobi(
                n, l, r, q, alpha, beta, delta, K, M, x, y, mu, lmd, lower, upper)
        else:
            reduced_cost, pricing_new_columns = pricing_warm_start(
                pricing_model, r_var, mu, s_var, lmd, t_var, delta, n, l, cx_var, cy_var)
        
        if counter - model_write_frequency >= last_model_write or counter == iterations:
            last_model_write = counter
            write_model(master_model,file_name,counter,pricing_model)

        print("Reduced Cost", reduced_cost)
        #print("New Columns Found", pricing_new_columns)
        
        # Check termination criteria
        if len(reduced_cost) == 0 or reduced_cost[0] >= -1e-2:
            write_model(master_model,file_name,counter,pricing_model)
            return terminate_helper(file_name, all_clusters, objectives, master_solutions, counter, slacks)

        # Prepare for next iteration
        warm_start_new_columns = []
        for solNum, sol in enumerate(pricing_new_columns):
            (cluster, old_t, old_dist, (old_xc, old_yc), bound, objVal) = sol
            if cluster in repeat_check:
                print("Not accepting repeated solution ", str(solNum), str(cluster))
                continue
            if objVal > -1e-2:
                print("Positive reduced cost", solNum, objVal)
                continue
            repeat_check.append(cluster)
            xc, yc, dist, old_dist_recalc, old_dist_recalc_array = calc_geometric_center_dist(cluster, x, y, old_xc, old_yc)

            print(counter, "Solution", solNum, "Pricing New cluster", cluster)
            print(counter, "Solution", solNum, dist)
            print("Compare", sum(old_dist), old_dist_recalc, dist, old_dist)
            #print("old_dist_1", old_dist)
            #print("old_dist_2", old_dist_recalc_array)
            #print("difference", list(np.array(old_dist) - np.array(old_dist_recalc_array)))
            #print("Compare center", (old_xc, old_yc), (xc,yc))

            new_t = t_value_correction(cluster, l, q, alpha, old_t)
            warm_start_new_columns.append((cluster, new_t, dist, (xc, yc), bound, objVal))
            all_clusters.append((cluster, new_t, dist, (xc, yc), bound, objVal))
            m += 1

    return terminate_helper(file_name, all_clusters, objectives, master_solutions, counter, slacks)


def terminate_helper(file_name, all_clusters, objectives, master_solutions, counter, slacks):
    clusters_mat = []
    distances_vec = []
    t_mat = []
    bounds = []
    objVals = []
    for i in all_clusters:
        distances_vec.append(i[2])
        clusters_mat.append(i[0] + i[1])
        t_mat.append(i[3])
        bounds.append(i[4])
        objVals.append(i[5])
    print(len(clusters_mat[0]))
    print(len(clusters_mat[-1]))

    clusters_mat = np.array(clusters_mat)
    distances_vec = np.array(distances_vec)
    t_mat = np.array(t_mat)
    np.savetxt("./model_matrix/"+file_name+"_t.txt", t_mat)
    np.savetxt("./model_matrix/"+file_name+"_clusters.txt", clusters_mat)
    np.savetxt("./model_matrix/"+file_name+"_distances.txt", distances_vec)
    np.savetxt("./model_matrix/"+file_name+"_bounds.txt", np.array(bounds))
    np.savetxt("./model_matrix/"+file_name+"_objVals.txt", np.array(objVals))
    np.savetxt("./model_matrix/"+file_name +
               "_slacks.txt", np.array(slacks))
    np.savetxt("./model_matrix/"+file_name +
               "_objectives.txt", np.array(objectives))
    
    max_length = max(len(sublist) for sublist in master_solutions)
    padded_list = [sublist + [0] * (max_length - len(sublist)) for sublist in master_solutions]
    master_solutions_export = np.array(padded_list)
    
    np.savetxt("./model_matrix/"+file_name +"_solutions.txt", master_solutions_export, fmt='%.5f')

    print("Terminate")
    print("Number of iterations", counter)
    print("Last objective:", objectives[-1])
    print("Last solution:", master_solutions[-1])
    print("All objectives:", objectives)
    print("All solutions:", master_solutions)
    print("Clusters:")
    for i in all_clusters:
        print(i)
    print("All slacks:", slacks)
    return all_clusters, objectives, master_solutions, counter, slacks


def calc_geometric_center_dist(cluster, x, y, old_xc, old_yc):
    xc = 0
    yc = 0
    size = sum(cluster)
    for j in range(len(cluster)):
        if cluster[j] == 1:
            xc += x[j]
            yc += y[j]
    xc = xc / size
    yc = yc / size
    dist = 0
    old_dist_recalc = 0
    old_dist_recalc_array = []

    for j in range(len(cluster)):
        if cluster[j] == 1:
            dist += ((xc - x[j]) ** 2 + (yc - y[j]) ** 2)
            aux = ((old_xc - x[j]) ** 2 + (old_yc - y[j]) ** 2)
            old_dist_recalc += aux
            old_dist_recalc_array.append(aux)
        else:
            old_dist_recalc_array.append(0)
    

    return xc, yc, dist, old_dist_recalc, old_dist_recalc_array


def initialize_clusters(X, K, l, alpha, beta, n, labels, M, lower, upper):
    # Set up labels info
    group_info = [set() for _ in range(l)]
    for i in range(n):
        group_info[int(labels[i])].add(i)

    # Initialize feasible solution
    obj, clusters, alpharep = solve_initial_feasible_solution(
        n, l, alpha, beta, K, M, lower, upper, group_info)

    clusters = clusters.T.astype(int).tolist()
    clusters_assign = [0 for _ in range(n)]
    for i, clus in enumerate(clusters):
        for j in range(n):
            if clus[j] == 1:
                clusters_assign[j] = int(i)

    # Calculate initial centers
    xc = [0 for _ in range(K)]
    yc = [0 for _ in range(K)]
    cluster_size = [0 for _ in range(K)]

    for i in range(n):
        k = clusters_assign[i]
        cluster_size[k] += 1
        xc[k] += X[i][0]
        yc[k] += X[i][1]

    for k in range(K):
        xc[k] /= cluster_size[k]
        yc[k] /= cluster_size[k]

    centers = [(xc[i], yc[i]) for i in range(K)]

    # Calculate initial distances
    dist = [0 for _ in range(K)]
    for i in range(n):
        k = clusters_assign[i]
        dist[k] += (X[i][0] - xc[k]) ** 2 + (X[i][1] - yc[k]) ** 2

    # Initialize q
    q = [[0 for _ in range(n)] for _ in range(l)]
    for i in range(n):
        label = int(labels[i])
        q[label][i] = 1

    # Initialize t
    t = alpharep.astype(int).tolist()

    return centers, dist, q, clusters, clusters_assign, t


def synthetic_data(n, K, seed):
    set_seed(seed)
    archetype = Archetype(n_clusters=K, dim=2, n_samples=n,
                          aspect_ref=1, aspect_maxmin=1, radius_maxmin=1, max_overlap=0.02, min_overlap=0.01)
    data_generator = DataGenerator(archetype=archetype)
    X, Y, archetype = data_generator.synthesize()
    return X, Y, archetype


def initialize_clusters_random(X, K, l, alpha, n, labels):
    # Calculate initial centers
    clusters_assign_random = np.random.choice(list(range(K)), size=n)
    xc = [0 for _ in range(K)]
    yc = [0 for _ in range(K)]
    cluster_size = [0 for _ in range(K)]

    for i in range(n):
        k = int(clusters_assign_random[i])
        cluster_size[k] += 1
        xc[k] += X[i][0]
        yc[k] += X[i][1]

    for k in range(K):
        xc[k] /= cluster_size[k]
        yc[k] /= cluster_size[k]

    dist = [0 for _ in range(K)]

    for i in range(n):
        k = int(clusters_assign_random[i])
        dist[k] += (X[i][0] - xc[k]) ** 2 + (X[i][1] - yc[k]) ** 2

    centers = [(xc[i], yc[i]) for i in range(K)]

    # Randomly assigning labels
    clusters_random = [[0 for _ in range(n)] for _ in range(K)]
    for i in range(n):
        k = int(clusters_assign_random[i])
        clusters_random[k][i] = 1

    # Initialize q
    q = [[0 for _ in range(n)] for _ in range(l)]
    for i in range(n):
        label = int(labels[i])
        q[label][i] = 1

    # Initialize t
    label_stats = [[0 for _ in range(K)] for _ in range(l)]
    t = [[0 for _ in range(K)] for _ in range(l)]
    for i in range(n):
        label = int(labels[i])
        k = int(clusters_assign_random[i])
        label_stats[label][k] += 1

    for i in range(l):
        for k in range(K):
            if label_stats[i][k] >= alpha * cluster_size[k]:
                t[i][k] = 1

    return centers, dist, q, clusters_random, t


def solve_initial_feasible_solution(n, l, alpha, beta, K, M, lower, upper, group_info):
    # Create a Gurobi model
    model = gp.Model("PricingProblem")
    model.Params.LogToConsole = 0
    model.Params.MIPFocus = 1

    # Create decision variables
    Z = model.addMVar((n, K), vtype=GRB.BINARY, name="Z")
    y = model.addMVar((l, K), vtype=GRB.BINARY, name="Y")

    # Objective function
    model.setObjective(y.sum(), GRB.MAXIMIZE)

    # Constraints
    constraints = []

    for i in range(n):
        model.addConstr(gp.quicksum(Z[i][k] for k in range(K)) == 1)

    for g in range(l):
        for k in range(K):
            model.addConstr(gp.quicksum(Z[i][k] for i in group_info[g]) + M*(
                1-y[g][k]) >= alpha * gp.quicksum(Z[i][k] for i in range(n)))

    for g in range(l):
        model.addConstr(gp.quicksum(y[g][k] for k in range(K)) >= beta[g])

    for k in range(K):
        model.addConstr(gp.quicksum(Z[i][k] for i in range(n)) >= lower)
        model.addConstr(gp.quicksum(Z[i][k] for i in range(n)) <= upper)

    # Solve the problem
    model.optimize()

    # Print objective value
    # print('Objective:', model.objVal)

    # Print variable values
    # for var in model.getVars():
    # print(f"{var.varName} = {var.x}")

    # Print constraints
    # for constr in constraints:
    #   print(constr)

    return model.objVal, Z.x, y.x


def visualize_result(s, r, t, n, K, masterobj, optimal_values_Z, centers, objectives, X, labels, filename):
    optimal_clusters = []
    optimal_clusters_assign = [0 for _ in range(n)]
    optimal_centers = []
    counter = 0
    for i, clust in enumerate(optimal_values_Z):
        if clust == 1:
            optimal_clusters.append(s[i])
            for j in range(n):
                if s[i][j] == 1:
                    optimal_clusters_assign[j] = counter
            counter += 1
            optimal_centers.append(centers[i])

    print(optimal_clusters_assign)
    print(optimal_centers)

    plt.plot(objectives)
    plt.xlabel("Iteration")
    plt.ylabel("Objective")
    plt.title("Objectives of master problem (n="+str(n)+" k="+str(K)+")")
    plt.savefig("./outputs/"+filename+"_iter.png")

    fig, ax = plt.subplots(figsize=(6, 6), dpi=150)
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
    ax.scatter(X[:, 0], X[:, 1], c=labels, s=15, linewidth=1.0)
    xc = [i[0] for i in optimal_centers]
    yc = [i[1] for i in optimal_centers]
    ax.scatter(xc, yc, marker='P', c=list(range(K)), s=50, linewidth=1.0)
    for i in range(n):
        x = (X[i, 0], optimal_centers[optimal_clusters_assign[i]][0])
        y = (X[i, 1], optimal_centers[optimal_clusters_assign[i]][1])
        ax.plot(x, y, c=colors[optimal_clusters_assign[i]], alpha=0.5)

    plt.title("Labels")
    plt.xlabel('X1')
    plt.ylabel('X2').set_rotation(0)
    plt.axis('equal')
    plt.savefig("./outputs/"+filename+"_scatter.png")

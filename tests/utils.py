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

    # Print objective value
    #print("Objective:", model.objVal)

    # Print variable values
    # for i, var in enumerate(model.getVars()):
        #print(f"{var.varName} = {var.x}")

    # Print dual variables
    #print("Dual values:")
    #for constr in model.getConstrs():
        #print(f"{constr.ConstrName}: {constr.Pi}")

    constraints = list(model.getConstrs())

    mu = [cons_i.Pi for cons_i in constraints[:n]]

    lmd = [cons_g.Pi for cons_g in constraints[n : n + l]]

    delta = constraints[n + l].Pi

    # for cons_i in constraints[:n]:
    #   mu.append(cons_i.Pi)

    # lmd = []
    # for cons_g in constraints[n:n+l]:
    #   lmd.append(cons_g.Pi)

    optimal_values_Z = [(Z[k].x) for k in range(m)]

    optimal_slack = []
    optimal_slack_sum = -1
    if slack:
       optimal_slack = [(slack_var[k].x) for k in range(n)]
       optimal_slack_sum = sum(optimal_slack)

    return model, mu, lmd, model.objVal, optimal_values_Z, delta, Z, slack_var, optimal_slack, optimal_slack_sum


def master_warm_start(model, Z, m, n, l, new_r_list, optimal_values_s_list, optimal_values_t_list, slack = False, slack_var = None):
  for solNum in range(len(new_r_list)):
    new_r = new_r_list[solNum]
    constrs = model.getConstrs()
    optimal_values_s = optimal_values_s_list[solNum].copy()
    for i in optimal_values_t_list[solNum]:
      optimal_values_s.append(i) # new column
    optimal_values_s.append(1)
    new_z = model.addVar(vtype=GRB.CONTINUOUS, name="Z["+str(m)+"]", column = gp.Column(optimal_values_s,constrs[:n+l+1]))
    Z += [new_z]
    model.setObjective(model.getObjective() + new_z * new_r, GRB.MINIMIZE)
  return master_optimize(model,m,n,l,Z,slack,slack_var)


def solve_master_problem_gurobi(n, m, l, r, s, t, beta, K, slack = False):
    # Create a Gurobi model
    model = gp.Model("MasterProblem")
    model.Params.LogToConsole = 0

    # Create decision variables
    Z = []
    for i in range(m):
        Z.append(model.addVar(vtype=GRB.CONTINUOUS, name="Z"))
    # Z = model.addMVar(m, vtype=GRB.CONTINUOUS, name="Z")

    slack_var = [model.addVar(vtype=GRB.CONTINUOUS, name="Slack") for _ in range(n)]
    # Set objective function
    if slack == False:
        model.setObjective(gp.quicksum(Z[i] * r[i] for i in range(m)), GRB.MINIMIZE)
    else:
        model.setObjective(gp.quicksum(Z[i] * r[i] for i in range(m)) + 20 * gp.quicksum(slack_var[i] for i in range(n)), GRB.MINIMIZE)

    # Constraints
    constraint1 = []
    constraint2 = []

    if slack == False:
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
                    gp.quicksum(s[k][i] * Z[k] for k in range(m)) + slack_var[i]== 1,
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
        model.addConstr(gp.quicksum(Z[k] for k in range(m)) == K, name="Constraint3")
    ]

    # for k in range(m):
    #     model.addConstr(Z[k] <= 1, name="Constraint4_"+str(k))
    #     model.addConstr(Z[k] >= 0, name="Constraint5_"+str(k))

    return master_optimize(model, m, n, l, Z, slack, slack_var)


def solve_master_problem_integer(n, m, l, r, s, t, beta, K):
    # Create a Gurobi model
    model = gp.Model("MasterProblemInteger")
    model.Params.LogToConsole = 0

    # Create decision variables
    Z = model.addMVar(m, vtype=GRB.BINARY, name="Z")

    # Set objective function
    model.setObjective(gp.quicksum(Z[i] * r[i] for i in range(m)), GRB.MINIMIZE)

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
        model.addConstr(gp.quicksum(Z[k] for k in range(m)) == K, name="Constraint3")
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


def pricing_warm_start(model,r_var,mu,s_var,lmd,t_var,delta,n,l,cx_var,cy_var):
  objective = gp.quicksum(r_var[i] for i in range(n)) \
                - gp.quicksum(mu[i] * s_var[i] for i in range(n)) \
                - gp.quicksum(lmd[g] * t_var[g] for g in range(l)) \
                - delta
  model.setObjective(objective,GRB.MINIMIZE)
  model.optimize()
  # Print objective value
  # print('Objective:', model.objVal)

  # print("Number of solutions", model.SolCount)
  nSolutions = model.SolCount

  objectives = []
  optimal_values_s = []
  optimal_values_r = []
  optimal_values_t = []
  optimal_center = []

  for e in range(nSolutions):
        # print("Solution Number",e)
        model.setParam(GRB.Param.SolutionNumber, e)
        # print("Objective", model.PoolObjVal)
        objectives.append(model.PoolObjVal)
        # Print variable values
        # for var in model.getVars():
        #   print(f"{var.varName} = {var.Xn}")

        optimal_values_s.append([int(np.round(s_var[i].Xn)) for i in range(n)])
        optimal_values_r.append([float(r_var[i].Xn) for i in range(n)])
        optimal_values_t.append([int(np.round(t_var[g].Xn)) for g in range(l)])
        optimal_center.append((cx_var.x,cy_var.Xn))

  return objectives,optimal_values_s, optimal_values_r, optimal_values_t, optimal_center


def solve_pricing_problem_gurobi(n, l, r, q, alpha, beta, delta, K, M, x, y, mu, lmd, lower, upper):
    # Create a Gurobi model
    model = gp.Model("PricingProblem")
    model.Params.PoolSearchMode = 2
    model.Params.PoolSolutions = 10
    model.Params.TimeLimit = 20
    model.Params.MIPGap = 0.1
    #model.Params.LogToConsole = 0

    # Create decision variables
    r = model.addMVar(n, vtype=GRB.CONTINUOUS, name="R")
    s = model.addMVar(n, vtype=GRB.BINARY, name="S")
    t = model.addMVar(l, vtype=GRB.BINARY, name="t")
    cx = model.addVar(vtype=GRB.CONTINUOUS, lb = -100, name="cx")
    cy = model.addVar(vtype=GRB.CONTINUOUS, lb = -100, name="cy")

    # Objective function

    objective = gp.quicksum(r[i] for i in range(n)) \
                - gp.quicksum(mu[i] * s[i] for i in range(n)) \
                - gp.quicksum(lmd[g] * t[g] for g in range(l)) \
                - delta
    model.setObjective(objective , GRB.MINIMIZE)

    # Constraints
    constraints = []

    for g in range(l):
      constraints.append(model.addConstr(gp.quicksum(q[g][i] * s[i] for i in range(n)) + M*(1-t[g]) >= alpha * gp.quicksum(s[i] for i in range(n)), name="Constraint1"))

    for i in range(n):
      constraints.append(model.addConstr(r[i] + M*(1-s[i]) >= (x[i] - cx)**2 + (y[i] - cy)**2, name="Constraint2"))
      constraints.append(model.addConstr(r[i] >= 0, name="Constraint3"))

    constraints.append(model.addConstr(gp.quicksum(s[i] for i in range(n)) >= lower, name="Constraint3"))
    constraints.append(model.addConstr(gp.quicksum(s[i] for i in range(n)) <= upper, name="Constraint4"))

    # Solve the problem
    model.optimize()

    # Print objective value
    # print('Objective:', model.objVal)

    print("Number of solutions", model.SolCount)
    nSolutions = model.SolCount


    # for e in range(nSolutions):
    #       print("Solution Number",e)
    #       model.setParam(GRB.Param.SolutionNumber, e)
    #       print("Objective", model.PoolObjVal)
    #       # Print variable values
    #       for var in model.getVars():
    #         print(f"{var.varName} = {var.Xn}")

    # Print variable values
    # for var in model.getVars():
    #   print(f"{var.varName} = {var.Xn}")

    # Print constraints
    # for constr in constraints:
    #   print(constr)

    optimal_values_s = [int(np.round(s[i].x)) for i in range(n)]
    optimal_values_r = [float(r[i].x) for i in range(n)]
    optimal_values_t = [int(np.round(t[g].x)) for g in range(l)]
    optimal_center = (cx.x,cy.x)

    return model, [model.objVal], [optimal_values_s], [optimal_values_r], [optimal_values_t], [optimal_center], r, s, t, cx, cy


def t_value_correction(new_cluster, l, q, alpha, optimal_values_t):
    new_cluster_size = sum(new_cluster)
    new_cluster_arr = np.array(new_cluster)
    for i in range(l):
        count = np.sum(new_cluster_arr & np.array(q[i]))
        if count >= alpha * new_cluster_size:
            if optimal_values_t[i] == 0:
                # print("Warning: t value not correctly calculated")
                optimal_values_t[i] = 1

def main_loop(iterations,K,n,m,l,r,beta,s,t,alpha,M,q,lower,upper,x,y,optimal_centers):
  reduced_cost = 1
  counter = 0
  master_model = None
  pricing_model = None
  Z = None
  pbar = tqdm(total=iterations)
  objectives = []
  times = []
  slacks = []
  while counter < iterations:
    counter += 1
    pbar.update(1)
    print("Iteration #" + str(counter))
    time = datetime.now()
    times.append(time)
    print("Time", time)
    if not master_model:
      master_model, mu, lmd, masterobj, optimal_values_Z, delta, Z, slack_var, optimal_slack, optimal_slack_sum = solve_master_problem_gurobi(n, m, l, r, s, t, beta, K, slack = True)
      objectives.append(masterobj)
    else:
      master_model, mu, lmd, masterobj, optimal_values_Z, delta, Z, slack_var, optimal_slack, optimal_slack_sum = master_warm_start(master_model, Z, m, n, l, new_r, optimal_values_s, optimal_values_t, True, slack_var)
      objectives.append(masterobj)
    slacks.append(optimal_slack_sum)
    print(counter, "Slack variables", optimal_slack)
    print(counter, "Sum of Slack Variables", optimal_slack_sum)
    print(counter, "Master Objective", masterobj)
    print(counter, "Master Solution", optimal_values_Z)
    print(counter, "Master Dual", mu)
    if not pricing_model:
      pricing_model, reduced_cost, optimal_values_s, optimal_values_r, optimal_values_t, optimal_center,r_var, s_var, t_var, cx_var, cy_var = solve_pricing_problem_gurobi(n, l, r, q, alpha, beta, delta, K, M, x, y, mu, lmd, lower, upper)
    else:
      reduced_cost, optimal_values_s, optimal_values_r, optimal_values_t, optimal_center = pricing_warm_start(pricing_model,r_var,mu,s_var,lmd,t_var,delta,n,l,cx_var,cy_var)
    
    new_r = []
    repeat_check = []
    print("Reduced Cost", reduced_cost)
    print("Solutions Found", optimal_values_s)
    if reduced_cost[0] >= -1e-2:
        print("Terminate")
        print("Number of iterations", counter)
        print("Objective:",masterobj)
        print("Z:")
        print(optimal_values_Z)
        print("s:")
        print(s)
        print("Clusters:")
        for i in range(len(s)):
          if optimal_values_Z[i] > 0:
            print(s[i])
        print("Slacks",slacks)
        return s, r, t, masterobj, optimal_values_Z, optimal_centers, objectives
    for solNum in range(len(reduced_cost)):
      if optimal_values_s[solNum] in repeat_check or optimal_values_s[solNum] in s:
        continue
      repeat_check.append(optimal_values_s[solNum])
      xc = 0
      yc = 0
      size = sum(optimal_values_s[solNum])
      for j in range(len(optimal_values_s[solNum])):
        if optimal_values_s[solNum][j] == 1:
          xc += x[j]
          yc += y[j]
      xc = xc / size
      yc = yc / size
      dist = 0
      for j in range(len(optimal_values_s[solNum])):
        if optimal_values_s[solNum][j] == 1:
          dist += (xc - x[j]) ** 2 + (yc - y[j]) ** 2
      optimal_centers.append((xc,yc))
      print(counter, "Solution", solNum, "Pricing New cluster", optimal_values_s[solNum])
      print(counter, "Solution", solNum, dist)
      s.append(optimal_values_s[solNum])
      new_r.append(dist)
      r.append(dist)
      t_value_correction(optimal_values_s[solNum],l,q,alpha,optimal_values_t[solNum])
      for g in range(l):
        t[g].append(optimal_values_t[solNum][g])
      m += 1

  #masterobj, optimal_values_Z = solve_master_problem_integer(n, m, l, r, s, t, beta, K)

  print("Slacks",slacks)

  return s, r, t, masterobj, optimal_values_Z, optimal_centers, objectives
  

def initialize_clusters(X,K,l,alpha,beta,n,labels,M,lower,upper):
  #Set up labels info
  group_info = [set() for _ in range(l)]
  for i in range(n):
    group_info[int(labels[i])].add(i)
  
  #Initialize feasible solution
  obj,clusters,alpharep = solve_initial_feasible_solution(n, l, alpha, beta, K, M, lower, upper, group_info)

  clusters = clusters.T.astype(int).tolist()
  clusters_assign = [0 for _ in range(n)]
  for i,clus in enumerate(clusters):
    for j in range(n):
      if clus[j] == 1:
        clusters_assign[j] = int(i)

  #Calculate initial centers
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

  centers = [(xc[i],yc[i]) for i in range(K)]

  #Calculate initial distances
  dist = [0 for _ in range(K)]
  for i in range(n):
    k = clusters_assign[i]
    dist[k] += (X[i][0] - xc[k]) **2 + (X[i][1] - yc[k]) **2

  # Initialize q
  q = [[0 for _ in range(n)] for _ in range(l)]
  for i in range(n):
    label = int(labels[i])
    q[label][i] = 1

  # Initialize t
  t = alpharep.astype(int).tolist()

  return centers, dist, q, clusters, clusters_assign, t

def synthetic_data(n,K,seed):
  set_seed(seed)
  archetype = Archetype(n_clusters=K, dim=2, n_samples=n,
                             aspect_ref=1, aspect_maxmin=1, radius_maxmin=1, max_overlap = 0.02, min_overlap = 0.01)
  data_generator = DataGenerator(archetype=archetype)
  X, Y, archetype = data_generator.synthesize()
  return X,Y,archetype

def initialize_clusters_random(X,K,l,alpha,n,labels):
  #Calculate initial centers
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
    dist[k] += (X[i][0] - xc[k]) **2 + (X[i][1] - yc[k]) **2

  centers = [(xc[i],yc[i]) for i in range(K)]

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
    Z = model.addMVar((n,K), vtype=GRB.BINARY, name="Z")
    y = model.addMVar((l,K), vtype=GRB.BINARY, name="Y")

    # Objective function
    model.setObjective(0, GRB.MINIMIZE)

    # Constraints
    constraints = []

    for i in range(n):
      model.addConstr(gp.quicksum(Z[i][k] for k in range(K)) == 1)

    for g in range(l):
      for k in range(K):
        model.addConstr(gp.quicksum(Z[i][k] for i in group_info[g]) + M*(1-y[g][k]) >= alpha * gp.quicksum(Z[i][k] for i in range(n)))

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
    #for var in model.getVars():
      #print(f"{var.varName} = {var.x}")

    # Print constraints
    # for constr in constraints:
    #   print(constr)

    return model.objVal, Z.x, y.x

def visualize_result(s, r, t, n, K, masterobj, optimal_values_Z, centers, objectives, X, labels,filename):
  optimal_clusters = []
  optimal_clusters_assign = [0 for _ in range(n)]
  optimal_centers = []
  counter = 0
  for i,clust in enumerate(optimal_values_Z):
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
  
  fig, ax = plt.subplots(figsize=(6,6), dpi=150)
  colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
  ax.scatter(X[:,0], X[:,1], c=labels, s=15, linewidth=1.0)
  xc = [i[0] for i in optimal_centers]
  yc = [i[1] for i in optimal_centers]
  ax.scatter(xc, yc, marker='P', c=list(range(K)), s=50, linewidth=1.0)
  for i in range(n):
    x = (X[i,0],optimal_centers[optimal_clusters_assign[i]][0])
    y = (X[i,1],optimal_centers[optimal_clusters_assign[i]][1])
    ax.plot(x,y, c = colors[optimal_clusters_assign[i]], alpha = 0.5)

  plt.title("Labels")
  plt.xlabel('X1')
  plt.ylabel('X2').set_rotation(0)
  plt.axis('equal')
  plt.savefig("./outputs/"+filename+"_scatter.png")


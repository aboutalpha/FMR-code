import numpy as np
import gurobipy as gp
from gurobipy import GRB
from repliclust import set_seed, Archetype, DataGenerator
import matplotlib.pyplot as plt


def master_optimize(model, m, n, l, Z):
    # Solve the problem
    model.optimize()

    # Print objective value
    print("Objective:", model.objVal)

    # Print variable values
    for i, var in enumerate(model.getVars()):
        print(f"{var.varName} = {var.x}")

    # Print dual variables
    print("Dual values:")
    for constr in model.getConstrs():
        print(f"{constr.ConstrName}: {constr.Pi}")

    constraints = list(model.getConstrs())

    mu = [cons_i.Pi for cons_i in constraints[:n]]

    lmd = [cons_g.Pi for cons_g in constraints[n : n + l]]

    delta = constraints[n + l].Pi

    # for cons_i in constraints[:n]:
    #   mu.append(cons_i.Pi)

    # lmd = []
    # for cons_g in constraints[n:n+l]:
    #   lmd.append(cons_g.Pi)

    optimal_values_Z = [int(Z[k].x) for k in range(m)]

    return model, mu, lmd, model.objVal, optimal_values_Z, delta, Z


def master_warm_start(model, Z, m, n, l, new_r, optimal_values_s, optimal_values_t):
    constrs = model.getConstrs()
    optimal_values_s = optimal_values_s.copy()
    print("optimal_values_t", optimal_values_t)
    for i in optimal_values_t:
        optimal_values_s.append(i)  # new column
    optimal_values_s.append(1)
    print(optimal_values_s)
    print(constrs[: n + l + 1])
    print(gp.Column(optimal_values_s, constrs[: n + l + 1]))
    new_z = model.addVar(
        vtype=GRB.CONTINUOUS,
        name="Z[" + str(m) + "]",
        column=gp.Column(optimal_values_s, constrs[: n + l + 1]),
    )
    Z += [new_z]
    model.setObjective(model.getObjective() + new_z * new_r, GRB.MINIMIZE)
    print(model.getObjective())
    return master_optimize(model, m, n, l, Z)


def solve_master_problem_gurobi(n, m, l, r, s, t, beta, K):
    # Create a Gurobi model
    model = gp.Model("MasterProblem")
    # model.Params.LogToConsole = 0

    # Create decision variables
    Z = []
    for i in range(m):
        Z.append(model.addVar(vtype=GRB.CONTINUOUS, name="Z"))
    # Z = model.addMVar(m, vtype=GRB.CONTINUOUS, name="Z")

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

    # for k in range(m):
    #     model.addConstr(Z[k] <= 1, name="Constraint4_"+str(k))
    #     model.addConstr(Z[k] >= 0, name="Constraint5_"+str(k))

    return master_optimize(model, m, n, l, Z)


def solve_master_problem_integer(n, m, l, r, s, t, beta, K):
    # Create a Gurobi model
    model = gp.Model("MasterProblemInteger")
    # model.Params.LogToConsole = 0

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
    print("Objective:", model.objVal)

    # Print variable values
    for i, var in enumerate(model.getVars()):
        print(f"{var.varName} = {var.x}")

    optimal_values_Z = [int(Z[k].x) for k in range(m)]

    return model.objVal, optimal_values_Z


def pricing_warm_start(
    model, r_var, mu, s_var, lmd, t_var, delta, n, l, cx_var, cy_var
):
    objective = (
        gp.quicksum(r_var[i] for i in range(n))
        - gp.quicksum(mu[i] * s_var[i] for i in range(n))
        - gp.quicksum(lmd[g] * t_var[g] for g in range(l))
        - delta
    )
    model.setObjective(objective, GRB.MINIMIZE)
    model.optimize()
    # Print objective value
    print("Objective:", model.objVal)

    # Print variable values
    for var in model.getVars():
        print(f"{var.varName} = {var.x}")

    # Print constraints
    # for constr in constraints:
    #   print(constr)

    optimal_values_s = [int(np.round(s_var[i].x)) for i in range(n)]
    optimal_values_r = [float(r_var[i].x) for i in range(n)]
    optimal_values_t = [int(np.round(t_var[g].x)) for g in range(l)]
    optimal_center = (cx_var.x, cy_var.x)

    return (
        model.objVal,
        optimal_values_s,
        optimal_values_r,
        optimal_values_t,
        optimal_center,
    )


def solve_pricing_problem_gurobi(
    n, l, r, q, alpha, beta, delta, K, M, x, y, mu, lmd, lower, upper
):
    # Create a Gurobi model
    model = gp.Model("PricingProblem")
    # model.Params.LogToConsole = 0

    # Create decision variables
    r = model.addMVar(n, vtype=GRB.CONTINUOUS, name="R")
    s = model.addMVar(n, vtype=GRB.BINARY, name="S")
    t = model.addMVar(l, vtype=GRB.BINARY, name="t")
    cx = model.addVar(vtype=GRB.CONTINUOUS, lb=-100, name="cx")
    cy = model.addVar(vtype=GRB.CONTINUOUS, lb=-100, name="cy")

    # Objective function

    objective = (
        gp.quicksum(r[i] for i in range(n))
        - gp.quicksum(mu[i] * s[i] for i in range(n))
        - gp.quicksum(lmd[g] * t[g] for g in range(l))
        - delta
    )
    model.setObjective(objective, GRB.MINIMIZE)

    # Constraints
    constraints = []

    for g in range(l):
        constraints.append(
            model.addConstr(
                gp.quicksum(q[g][i] * s[i] for i in range(n)) + M * (1 - t[g])
                >= alpha * gp.quicksum(s[i] for i in range(n)),
                name="Constraint1",
            )
        )

    for i in range(n):
        constraints.append(
            model.addConstr(
                r[i] + M * (1 - s[i]) >= (x[i] - cx) ** 2 + (y[i] - cy) ** 2,
                name="Constraint2",
            )
        )
        constraints.append(model.addConstr(r[i] >= 0, name="Constraint3"))

    constraints.append(
        model.addConstr(
            gp.quicksum(s[i] for i in range(n)) >= lower, name="Constraint3"
        )
    )
    constraints.append(
        model.addConstr(
            gp.quicksum(s[i] for i in range(n)) <= upper, name="Constraint4"
        )
    )

    # Solve the problem
    model.optimize()

    # Print objective value
    print("Objective:", model.objVal)

    # Print variable values
    for var in model.getVars():
        print(f"{var.varName} = {var.x}")

    # Print constraints
    # for constr in constraints:
    #   print(constr)

    optimal_values_s = [int(np.round(s[i].x)) for i in range(n)]
    optimal_values_r = [float(r[i].x) for i in range(n)]
    optimal_values_t = [int(np.round(t[g].x)) for g in range(l)]
    optimal_center = (cx.x, cy.x)

    return (
        model,
        model.objVal,
        optimal_values_s,
        optimal_values_r,
        optimal_values_t,
        optimal_center,
        r,
        s,
        t,
        cx,
        cy,
    )


def t_value_correction(new_cluster, l, q, alpha, optimal_values_t):
    new_cluster_size = sum(new_cluster)
    new_cluster_arr = np.array(new_cluster)
    for i in range(l):
        count = np.sum(new_cluster_arr & np.array(q[i]))
        if count >= alpha * new_cluster_size:
            if optimal_values_t[i] == 0:
                print("Warning: t value not correctly calculated")
                optimal_values_t[i] = 1


def main_loop(
    iterations,
    K,
    n,
    m,
    l,
    r,
    beta,
    s,
    t,
    alpha,
    M,
    q,
    lower,
    upper,
    x,
    y,
    optimal_centers,
):
    reduced_cost = 1
    counter = 1
    master_model = None
    pricing_model = None
    Z = None
    objectives = []
    while counter < iterations:
        print("Iteration #" + str(counter))
        print("s:", s)
        print("r:", r)
        print("t:", t)
        counter += 1
        if not master_model:
            master_model, mu, lmd, masterobj, optimal_values_Z, delta, Z = (
                solve_master_problem_gurobi(n, m, l, r, s, t, beta, K)
            )
            objectives.append(masterobj)
        else:
            print("Master problem warm start")
            master_model, mu, lmd, masterobj, optimal_values_Z, delta, Z = (
                master_warm_start(
                    master_model, Z, m, n, l, new_r, optimal_values_s, optimal_values_t
                )
            )
            objectives.append(masterobj)
        if not pricing_model:
            (
                pricing_model,
                reduced_cost,
                optimal_values_s,
                optimal_values_r,
                optimal_values_t,
                optimal_center,
                r_var,
                s_var,
                t_var,
                cx_var,
                cy_var,
            ) = solve_pricing_problem_gurobi(
                n, l, r, q, alpha, beta, delta, K, M, x, y, mu, lmd, lower, upper
            )
        else:
            print("Pricing problem warm start")
            (
                reduced_cost,
                optimal_values_s,
                optimal_values_r,
                optimal_values_t,
                optimal_center,
            ) = pricing_warm_start(
                pricing_model, r_var, mu, s_var, lmd, t_var, delta, n, l, cx_var, cy_var
            )

        optimal_centers.append(optimal_center)
        print("New cluster found")
        print(optimal_values_s)
        print("New optimal_values_t")
        print(optimal_values_t)
        if reduced_cost >= -1e-2:
            print("Terminate")
            print("Number of iterations", counter)
            print("Objective:", masterobj)
            print("Z:")
            print(optimal_values_Z)
            print("s:")
            print(s)
            print("Clusters:")
            for i in range(len(s)):
                if optimal_values_Z[i] > 0:
                    print(s[i])
            break
        if optimal_values_s in s:
            # raise Exception("Error: Repetition")
            print("Repetition found. Terminate.")
            print("Number of iterations", counter)
            print("Objective:", masterobj)
            print("Z:")
            print(optimal_values_Z)
            print("s:")
            print(s)
            print("Clusters:")
            for i in range(len(s)):
                if optimal_values_Z[i] > 0:
                    print(s[i])
        s.append(optimal_values_s)
        new_r = sum(optimal_values_r)
        r.append(new_r)
        t_value_correction(optimal_values_s, l, q, alpha, optimal_values_t)
        for g in range(l):
            t[g].append(optimal_values_t[g])
        m += 1

    masterobj, optimal_values_Z = solve_master_problem_integer(
        n, m, l, r, s, t, beta, K
    )

    return s, r, t, masterobj, optimal_values_Z, optimal_centers, objectives

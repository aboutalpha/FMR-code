import numpy as np
import gurobipy as gp
import matplotlib.pyplot as plt
from gurobipy import GRB
import pandas as pd
import seaborn as sns
from tqdm.notebook import tqdm
from utils import *

for file_name in ["test11_1_slack"]:
    for sol_num in ["201","401","601","801","1001","1201","1401","1601","1801"]:
        print(file_name)
        #test 11
        n = 200
        K = 5
        seed = 7
        l = 3
        alpha = 0.51
        beta = [1, 1, 2]
        lower = 5
        upper = n
        M = 1e3
        np.random.seed(seed)

        groups = [0,1,2]
        p = [0.25,0.15,0.6]
        labels = np.random.choice(groups, p=p, size=n)

        X, Y, archetype = synthetic_data(n, K, seed)
        centers, dist, q, clusters, clusters_assign, t = initialize_clusters(X,K,l,alpha,beta,n,labels,M,lower,upper)

        model = gp.read("./model_write/" + file_name + "_master_out"+sol_num+".mps")
        constrs_len = len(model.getConstrs())
        #print(constrs_len)
        clusters = np.loadtxt("./model_matrix/"+file_name+"_clusters.txt")
        distances = np.loadtxt("./model_matrix/"+file_name+"_distances.txt")
        slacks = np.loadtxt("./model_matrix/"+file_name+"_slacks.txt")
        solutions = np.loadtxt("./model_matrix/"+file_name+"_solutions.txt")
        objectives = np.loadtxt("./model_matrix/"+file_name+"_objectives.txt")
        new_centers = np.loadtxt("./model_matrix/"+file_name+"_t.txt")
        new_centers = [(i[0],i[1]) for i in new_centers]

        clusters = np.concatenate((clusters,np.ones(clusters.shape[0]).reshape(-1,1)),axis=1)
        A = [[model.getCoeff(constr, var) for var in model.getVars()] for constr in model.getConstrs()]
        b = [constr.rhs for constr in model.getConstrs()]
        c = [var.obj for var in model.getVars()]
        induced_mat = np.concatenate((clusters[:K,:],np.eye(constrs_len-1,constrs_len),clusters[K:,:]),axis=0).T
        A = np.array(A)

        additional_cluster_in_the_last_round = induced_mat.shape[1] - A.shape[1]

        m = clusters.shape[0] - additional_cluster_in_the_last_round
        r = distances.tolist()[:m]
        s = clusters[:m,:n].tolist()
        new_t = clusters[:m,n:n+l].T.tolist()

        iters = 10
        main_loop(file_name+"_recon_"+sol_num+"_"+str(iters), iters, K, n, m, l, r, beta, s, new_t, alpha, M, q, lower, upper, X[:, 0], X[:, 1], new_centers,slack = (20,100,False))


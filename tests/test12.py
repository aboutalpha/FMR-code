from utils import *
from gurobipy import Env

env = Env()

for i in [True, False]:
    test_name = "test12_1"
    
    if i :
        test_name += "_slack"
    
    print("New Task")
    
    iters_bound = 3000
    slack1 = 20
    slack2 = 150
    
    n = 300
    K = 6
    seed = 10
    l = 4
    alpha = 0.51
    beta = [1, 1, 1, 1]
    lower = 5
    upper = n
    M = 1e3
    np.random.seed(seed)

    groups = [0,1,2,3]
    p = [0.2,0.2,0.5,0.1]
    labels = np.random.choice(groups, p=p, size=n)

    print(i,iters_bound,slack1,slack2,n,K,seed,l,alpha,beta,lower,upper,M,groups,p)

    X, Y, archetype = synthetic_data(n, K, seed)
    centers, dist, q, clusters, clusters_assign, t = initialize_clusters(
        X, K, l, alpha, beta, n, labels, M, lower, upper)

    r = dist.copy()
    s = clusters.copy()
    m = K

    main_loop(test_name, iters_bound, K, n, m, l, r, beta, s, t, alpha,
            M, q, lower, upper, X[:, 0], X[:, 1], centers, slack = (slack1,slack2,i))

env.dispose()

from utils import *
from gurobipy import Env

env = Env()
env.setParam('LogToConsole', 0)
env.start()

n = 200
K = 5
seed = 5
l = 4
alpha = 0.51
beta = [1, 1, 1, 1]
lower = 5
upper = n
M = 1e3
np.random.seed(seed)
labels = np.random.choice([0, 1, 2, 3], p=[0.2, 0.2, 0.2, 0.4], size=n)

X, Y, archetype = synthetic_data(n, K, seed)
centers, dist, q, clusters, clusters_assign, t = initialize_clusters(
    X, K, l, alpha, beta, n, labels, M, lower, upper)

r = dist.copy()
s = clusters.copy()
m = K

main_loop("test9_slack10", 3000, K, n, m, l, r, beta, s, t, alpha,
          M, q, lower, upper, X[:, 0], X[:, 1], centers)

env.dispose()

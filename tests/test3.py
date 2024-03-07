from utils import *
from gurobipy import Env

env = Env()
env.setParam('OutputFlag', 0)
filename = "test3"
n = 200
K = 5
seed = 5
l = 3
alpha = 1/2
beta = [1,1,1]
lower = 2
upper = n
M = 1e6
np.random.seed(seed)
labels = np.random.choice([0,1,2], p= [0.1,0.2,0.7], size=n)

X,Y,archetype = synthetic_data(n,K,seed)
centers, dist, q, clusters, clusters_assign, t = initialize_clusters(X,K,l,alpha,beta,n,labels,M,lower,upper)

print(t)

r = dist.copy()
s = clusters.copy()
m = K

s, r, t, masterobj, optimal_values_Z, optimal_centers, objectives = main_loop(500,K,n,m,l,r,beta,s,t,alpha,M,q,lower,upper,X[:,0],X[:,1],centers)

visualize_result(s, r, t, n, K, masterobj, optimal_values_Z, centers, objectives, X, labels, filename)

env.dispose()

print("Result")
print("s:", s)
print()
print("r:", r)
print()
print("t:", t)
print()
print("masterobj:", masterobj)
print()
print("optimal_values_Z:", optimal_values_Z)
print()
print("optimal_centers:", optimal_centers)
print()
print("objectives:", objectives)

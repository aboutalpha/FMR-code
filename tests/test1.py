from utils import *

K = 2
n = 5
m = 6
l = 2
r = [0.5, 8 / 3, 1, 0.5, 1, 1]
beta = [1, 1]
#              A, B, C, D, E
s = [
    [1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [0, 0, 1, 0, 1],
    [0, 0, 1, 1, 0],
]
t = [[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1]]
alpha = 2 / 3
M = 1e3
q = [[1, 1, 0, 0, 0], [0, 0, 1, 1, 1]]
lower = 2
upper = n
x = [0, 0, 0, -1, 1]
y = [1, 0, -1, 0, 0]

main_loop(8, K, n, m, l, r, beta, s, t, alpha, M, q, lower, upper, x, y, [])

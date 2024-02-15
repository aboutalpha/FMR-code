Iteration #1
s: [[1, 1, 0, 0, 0], [0, 0, 1, 1, 1]]
r: [0.5, 2.6666666666666665]
t: [[1, 0], [0, 1]]
Warning for adding constraints: zero or small (< 1e-13) coefficients, ignored
Gurobi Optimizer version 11.0.0 build v11.0.0rc2 (mac64[rosetta2] - Darwin 23.2.0 23C71)

CPU model: Apple M1
Thread count: 8 physical cores, 8 logical processors, using up to 8 threads

Optimize a model with 12 rows, 2 columns and 13 nonzeros
Model fingerprint: 0xc5b5ffd3
Coefficient statistics:
  Matrix range     [1e+00, 1e+00]
  Objective range  [5e-01, 3e+00]
  Bounds range     [0e+00, 0e+00]
  RHS range        [1e+00, 2e+00]
Presolve removed 12 rows and 2 columns
Presolve time: 0.00s
Presolve: All rows and columns removed
Iteration    Objective       Primal Inf.    Dual Inf.      Time
       0    3.1666667e+00   0.000000e+00   0.000000e+00      0s

Solved in 0 iterations and 0.01 seconds (0.00 work units)
Optimal objective  3.166666667e+00
Objective: 3.1666666666666665
Z[0] = 1.0
Z[1] = 1.0
Dual values:
Constraint1_0: 0.5
Constraint1_1: 0.0
Constraint1_2: 2.6666666666666665
Constraint1_3: 0.0
Constraint1_4: 0.0
Constraint2_0: 0.0
Constraint2_1: 0.0
Constraint3: 0.0
Constraint4_0: 0.0
Constraint5_0: 0.0
Constraint4_1: 0.0
Constraint5_1: 0.0
Gurobi Optimizer version 11.0.0 build v11.0.0rc2 (mac64[rosetta2] - Darwin 23.2.0 23C71)

CPU model: Apple M1
Thread count: 8 physical cores, 8 logical processors, using up to 8 threads

Optimize a model with 9 rows, 14 columns and 27 nonzeros
Model fingerprint: 0xdd2980ce
Model has 5 quadratic constraints
Variable types: 7 continuous, 7 integer (7 binary)
Coefficient statistics:
  Matrix range     [3e-01, 1e+03]
  QMatrix range    [1e+00, 1e+00]
  QLMatrix range   [1e+00, 1e+03]
  Objective range  [5e-01, 3e+00]
  Bounds range     [1e+00, 1e+02]
  RHS range        [2e+00, 1e+03]
  QRHS range       [1e+03, 1e+03]
Presolve removed 3 rows and 1 columns
Presolve time: 0.00s
Presolved: 6 rows, 13 columns, 24 nonzeros
Presolved model has 1 quadratic constraint(s)
Variable types: 8 continuous, 5 integer (5 binary)

Root relaxation: objective -3.165667e+00, 4 iterations, 0.00 seconds (0.00 work units)

    Nodes    |    Current Node    |     Objective Bounds      |     Work
 Expl Unexpl |  Obj  Depth IntInf | Incumbent    BestBd   Gap | It/Node Time

     0     0   -3.16567    0    1          -   -3.16567      -     -    0s
H    0     0                    48002.083333   -3.16567   100%     -    0s
H    0     0                    47002.083333   -3.16567   100%     -    0s
H    0     0                      -2.1666665   -2.66667  23.1%     -    0s
*    0     0               0      -2.1666665   -2.66667  23.1%     -    0s
     0     0   -2.66667    0    2   -2.16667   -2.66667  23.1%     -    0s
     0     0   -2.66667    0    -   -2.16667   -2.66667  23.1%     -    0s
     0     0   -2.66667    0    2   -2.16667   -2.66667  23.1%     -    0s
     0     0   -2.66667    0    2   -2.16667   -2.66667  23.1%     -    0s
     0     0   -2.66667    0    2   -2.16667   -2.66667  23.1%     -    0s
     0     0   -2.66667    0    -   -2.16667   -2.66667  23.1%     -    0s
     0     0   -2.66667    0    2   -2.16667   -2.66667  23.1%     -    0s
     0     0   -2.66665    0    2   -2.16667   -2.66665  23.1%     -    0s
     0     0   -2.66643    0    2   -2.16667   -2.66643  23.1%     -    0s
     0     0   -2.66587    0    2   -2.16667   -2.66587  23.0%     -    0s
     0     0   -2.66459    0    2   -2.16667   -2.66459  23.0%     -    0s
     0     0   -2.66451    0    2   -2.16667   -2.66451  23.0%     -    0s
     0     0   -2.66442    0    2   -2.16667   -2.66442  23.0%     -    0s
     0     0   -2.66401    0    2   -2.16667   -2.66401  23.0%     -    0s
     0     0   -2.66375    0    2   -2.16667   -2.66375  22.9%     -    0s
     0     0   -2.66375    0    2   -2.16667   -2.66375  22.9%     -    0s
     0     2   -2.66375    0    2   -2.16667   -2.66375  22.9%     -    0s

Cutting planes:
  Implied bound: 1
  MIR: 1
  RLT: 1
  Relax-and-lift: 1

Explored 18 nodes (75 simplex iterations) in 0.05 seconds (0.00 work units)
Thread count was 8 (of 8 available processors)

Solution count 3: -2.16667 47002.1 48002.1 

Optimal solution found (tolerance 1.00e-04)
Best objective -2.166666538758e+00, best bound -2.166860797838e+00, gap 0.0090%
Objective: -2.1666665387579047
R[0] = 0.0
R[1] = 0.2501868758308904
R[2] = 0.24981325207787144
R[3] = 0.0
R[4] = 0.0
S[0] = 0.0
S[1] = 1.0
S[2] = 1.0
S[3] = 0.0
S[4] = 0.0
t[0] = 0.0
t[1] = 0.0
cx = 1.201573136327113e-05
cy = -0.500186811933676
New cluster found
[0, 1, 1, 0, 0]
Iteration #2
s: [[1, 1, 0, 0, 0], [0, 0, 1, 1, 1], [0, 1, 1, 0, 0]]
r: [0.5, 2.6666666666666665, 0.5000001279087618]
t: [[1, 0, 0], [0, 1, 0]]
Warning for adding constraints: zero or small (< 1e-13) coefficients, ignored
Gurobi Optimizer version 11.0.0 build v11.0.0rc2 (mac64[rosetta2] - Darwin 23.2.0 23C71)

CPU model: Apple M1
Thread count: 8 physical cores, 8 logical processors, using up to 8 threads

Optimize a model with 14 rows, 3 columns and 18 nonzeros
Model fingerprint: 0x8c6ec7dd
Coefficient statistics:
  Matrix range     [1e+00, 1e+00]
  Objective range  [5e-01, 3e+00]
  Bounds range     [0e+00, 0e+00]
  RHS range        [1e+00, 2e+00]
Presolve removed 14 rows and 3 columns
Presolve time: 0.00s
Presolve: All rows and columns removed
Iteration    Objective       Primal Inf.    Dual Inf.      Time
       0    3.1666667e+00   0.000000e+00   0.000000e+00      0s

Solved in 0 iterations and 0.00 seconds (0.00 work units)
Optimal objective  3.166666667e+00
Objective: 3.1666666666666665
Z[0] = 1.0
Z[1] = 1.0
Z[2] = 0.0
Dual values:
Constraint1_0: 0.5
Constraint1_1: 0.0
Constraint1_2: 0.0
Constraint1_3: 2.6666666666666665
Constraint1_4: 0.0
Constraint2_0: 0.0
Constraint2_1: 0.0
Constraint3: 0.0
Constraint4_0: 0.0
Constraint5_0: 0.0
Constraint4_1: 0.0
Constraint5_1: 0.0
Constraint4_2: 0.0
Constraint5_2: 0.0
Gurobi Optimizer version 11.0.0 build v11.0.0rc2 (mac64[rosetta2] - Darwin 23.2.0 23C71)

CPU model: Apple M1
Thread count: 8 physical cores, 8 logical processors, using up to 8 threads

Optimize a model with 9 rows, 14 columns and 27 nonzeros
Model fingerprint: 0x0d5c191b
Model has 5 quadratic constraints
Variable types: 7 continuous, 7 integer (7 binary)
Coefficient statistics:
  Matrix range     [3e-01, 1e+03]
  QMatrix range    [1e+00, 1e+00]
  QLMatrix range   [1e+00, 1e+03]
  Objective range  [5e-01, 3e+00]
  Bounds range     [1e+00, 1e+02]
  RHS range        [2e+00, 1e+03]
  QRHS range       [1e+03, 1e+03]
Presolve removed 3 rows and 1 columns
Presolve time: 0.00s
Presolved: 6 rows, 13 columns, 24 nonzeros
Presolved model has 1 quadratic constraint(s)
Variable types: 8 continuous, 5 integer (5 binary)

Root relaxation: objective -3.166667e+00, 2 iterations, 0.00 seconds (0.00 work units)

    Nodes    |    Current Node    |     Objective Bounds      |     Work
 Expl Unexpl |  Obj  Depth IntInf | Incumbent    BestBd   Gap | It/Node Time

H    0     0                      -2.1666666   -3.16667  46.2%     -    0s
*    0     0               0      -2.1666666   -3.16667  46.2%     -    0s
     0     0   -3.16667    0    -   -2.16667   -3.16667  46.2%     -    0s
     0     0   -3.16649    0    1   -2.16667   -3.16649  46.1%     -    0s
H    0     0                      -2.1666666   -3.16649  46.1%     -    0s
     0     0   -3.16586    0    2   -2.16667   -3.16586  46.1%     -    0s
     0     0   -2.81028    0    -   -2.16667   -2.81028  29.7%     -    0s
     0     0   -2.80531    0    2   -2.16667   -2.80531  29.5%     -    0s
     0     0   -2.80451    0    2   -2.16667   -2.80451  29.4%     -    0s
     0     0   -2.79971    0    2   -2.16667   -2.79971  29.2%     -    0s
     0     0   -2.79971    0    2   -2.16667   -2.79971  29.2%     -    0s
     0     0   -2.79967    0    2   -2.16667   -2.79967  29.2%     -    0s
     0     0   -2.79963    0    2   -2.16667   -2.79963  29.2%     -    0s
     0     0   -2.79924    0    2   -2.16667   -2.79924  29.2%     -    0s
     0     2   -2.79924    0    2   -2.16667   -2.79924  29.2%     -    0s

Cutting planes:
  Gomory: 1
  RLT: 1

Explored 34 nodes (78 simplex iterations) in 0.04 seconds (0.00 work units)
Thread count was 8 (of 8 available processors)

Solution count 1: -2.16667 

Optimal solution found (tolerance 1.00e-04)
Best objective -2.166666631249e+00, best bound -2.166694764123e+00, gap 0.0013%
Objective: -2.166666631249466
R[0] = 0.5000006584331231
R[1] = 0.0
R[2] = 0.0
R[3] = 0.49999937698407765
R[4] = 0.0
S[0] = 1.0
S[1] = 0.0
S[2] = -0.0
S[3] = 1.0
S[4] = -0.0
t[0] = 0.0
t[1] = 0.0
cx = -0.49998702208766016
cy = 0.49998638012979996
New cluster found
[1, 0, 0, 1, 0]
Iteration #3
s: [[1, 1, 0, 0, 0], [0, 0, 1, 1, 1], [0, 1, 1, 0, 0], [1, 0, 0, 1, 0]]
r: [0.5, 2.6666666666666665, 0.5000001279087618, 1.0000000354172007]
t: [[1, 0, 0, 0], [0, 1, 0, 0]]
Warning for adding constraints: zero or small (< 1e-13) coefficients, ignored
Gurobi Optimizer version 11.0.0 build v11.0.0rc2 (mac64[rosetta2] - Darwin 23.2.0 23C71)

CPU model: Apple M1
Thread count: 8 physical cores, 8 logical processors, using up to 8 threads

Optimize a model with 16 rows, 4 columns and 23 nonzeros
Model fingerprint: 0x57f8a483
Coefficient statistics:
  Matrix range     [1e+00, 1e+00]
  Objective range  [5e-01, 3e+00]
  Bounds range     [0e+00, 0e+00]
  RHS range        [1e+00, 2e+00]
Presolve removed 16 rows and 4 columns
Presolve time: 0.01s
Presolve: All rows and columns removed
Iteration    Objective       Primal Inf.    Dual Inf.      Time
       0    3.1666667e+00   0.000000e+00   0.000000e+00      0s

Solved in 0 iterations and 0.02 seconds (0.00 work units)
Optimal objective  3.166666667e+00
Objective: 3.1666666666666665
Z[0] = 1.0
Z[1] = 1.0
Z[2] = 0.0
Z[3] = 0.0
Dual values:
Constraint1_0: 0.0
Constraint1_1: 0.0
Constraint1_2: 0.0
Constraint1_3: 0.0
Constraint1_4: 2.6666666666666665
Constraint2_0: 0.5
Constraint2_1: 0.0
Constraint3: 0.0
Constraint4_0: 0.0
Constraint5_0: 0.0
Constraint4_1: 0.0
Constraint5_1: 0.0
Constraint4_2: 0.0
Constraint5_2: 0.0
Constraint4_3: 0.0
Constraint5_3: 0.0
Gurobi Optimizer version 11.0.0 build v11.0.0rc2 (mac64[rosetta2] - Darwin 23.2.0 23C71)

CPU model: Apple M1
Thread count: 8 physical cores, 8 logical processors, using up to 8 threads

Optimize a model with 9 rows, 14 columns and 27 nonzeros
Model fingerprint: 0x1da1a28a
Model has 5 quadratic constraints
Variable types: 7 continuous, 7 integer (7 binary)
Coefficient statistics:
  Matrix range     [3e-01, 1e+03]
  QMatrix range    [1e+00, 1e+00]
  QLMatrix range   [1e+00, 1e+03]
  Objective range  [5e-01, 3e+00]
  Bounds range     [1e+00, 1e+02]
  RHS range        [2e+00, 1e+03]
  QRHS range       [1e+03, 1e+03]
Presolve removed 2 rows and 0 columns
Presolve time: 0.00s
Presolved: 7 rows, 14 columns, 30 nonzeros
Presolved model has 1 quadratic constraint(s)
Variable types: 8 continuous, 6 integer (6 binary)

Root relaxation: objective -3.166667e+00, 6 iterations, 0.00 seconds (0.00 work units)

    Nodes    |    Current Node    |     Objective Bounds      |     Work
 Expl Unexpl |  Obj  Depth IntInf | Incumbent    BestBd   Gap | It/Node Time

H    0     0                      -1.8333333   -3.16667  72.7%     -    0s
*    0     0               0      -1.8333333   -3.16667  72.7%     -    0s
     0     0   -3.16667    0    -   -1.83333   -3.16667  72.7%     -    0s
     0     0   -3.16659    0    2   -1.83333   -3.16659  72.7%     -    0s
H    0     0                      -1.8889034   -3.16659  67.6%     -    0s
     0     0   -3.15749    0    3   -1.88890   -3.15749  67.2%     -    0s
     0     0   -2.96786    0    4   -1.88890   -2.96786  57.1%     -    0s
     0     0   -2.96786    0    4   -1.88890   -2.96786  57.1%     -    0s
     0     0   -2.96786    0    4   -1.88890   -2.96786  57.1%     -    0s
     0     0   -2.96786    0    4   -1.88890   -2.96786  57.1%     -    0s
     0     0   -2.89623    0    4   -1.88890   -2.89623  53.3%     -    0s
     0     0   -2.67113    0    4   -1.88890   -2.67113  41.4%     -    0s
     0     0   -2.67113    0    4   -1.88890   -2.67113  41.4%     -    0s
     0     0   -2.67113    0    4   -1.88890   -2.67113  41.4%     -    0s
     0     0   -2.66667    0    -   -1.88890   -2.66667  41.2%     -    0s
     0     0   -2.66667    0    2   -1.88890   -2.66667  41.2%     -    0s
     0     0   -2.66667    0    2   -1.88890   -2.66667  41.2%     -    0s
     0     0   -2.66667    0    -   -1.88890   -2.66667  41.2%     -    0s
     0     0   -2.66667    0    2   -1.88890   -2.66667  41.2%     -    0s
     0     0   -2.66652    0    4   -1.88890   -2.66652  41.2%     -    0s
     0     0   -2.66652    0    4   -1.88890   -2.66652  41.2%     -    0s
     0     0   -2.66651    0    4   -1.88890   -2.66651  41.2%     -    0s
     0     0   -2.66553    0    4   -1.88890   -2.66553  41.1%     -    0s
     0     0   -2.66528    0    4   -1.88890   -2.66528  41.1%     -    0s
     0     0   -2.65449    0    4   -1.88890   -2.65449  40.5%     -    0s
     0     0   -2.65382    0    4   -1.88890   -2.65382  40.5%     -    0s
     0     0   -2.65370    0    4   -1.88890   -2.65370  40.5%     -    0s
     0     2   -2.65370    0    4   -1.88890   -2.65370  40.5%     -    0s
H    3     2                      -2.1666665   -2.46786  13.9%   4.0    0s

Cutting planes:
  Cover: 1
  MIR: 5
  RLT: 1

Explored 18 nodes (116 simplex iterations) in 0.05 seconds (0.00 work units)
Thread count was 8 (of 8 available processors)

Solution count 2: -2.16667 -1.83333 

Optimal solution found (tolerance 1.00e-04)
Best objective -2.166666458553e+00, best bound -2.166843463578e+00, gap 0.0082%
Objective: -2.1666664585529345
R[0] = 0.0
R[1] = 0.2500514867755257
R[2] = 0.0
R[3] = 0.0
R[4] = 0.2499487213382064
S[0] = 0.0
S[1] = 1.0
S[2] = 0.0
S[3] = 0.0
S[4] = 1.0
t[0] = 0.0
t[1] = 0.0
cx = 0.5000513829818131
cy = -0.00010699674570996934
New cluster found
[0, 1, 0, 0, 1]
Iteration #4
s: [[1, 1, 0, 0, 0], [0, 0, 1, 1, 1], [0, 1, 1, 0, 0], [1, 0, 0, 1, 0], [0, 1, 0, 0, 1]]
r: [0.5, 2.6666666666666665, 0.5000001279087618, 1.0000000354172007, 0.500000208113732]
t: [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0]]
Warning for adding constraints: zero or small (< 1e-13) coefficients, ignored
Gurobi Optimizer version 11.0.0 build v11.0.0rc2 (mac64[rosetta2] - Darwin 23.2.0 23C71)

CPU model: Apple M1
Thread count: 8 physical cores, 8 logical processors, using up to 8 threads

Optimize a model with 18 rows, 5 columns and 28 nonzeros
Model fingerprint: 0xb65efe9b
Coefficient statistics:
  Matrix range     [1e+00, 1e+00]
  Objective range  [5e-01, 3e+00]
  Bounds range     [0e+00, 0e+00]
  RHS range        [1e+00, 2e+00]
Presolve removed 18 rows and 5 columns
Presolve time: 0.00s
Presolve: All rows and columns removed
Iteration    Objective       Primal Inf.    Dual Inf.      Time
       0    3.1666667e+00   0.000000e+00   0.000000e+00      0s

Solved in 0 iterations and 0.00 seconds (0.00 work units)
Optimal objective  3.166666667e+00
Objective: 3.1666666666666665
Z[0] = 1.0
Z[1] = 1.0
Z[2] = 0.0
Z[3] = 0.0
Z[4] = 0.0
Dual values:
Constraint1_0: 0.0
Constraint1_1: 0.0
Constraint1_2: 0.0
Constraint1_3: 0.0
Constraint1_4: 0.0
Constraint2_0: 0.5
Constraint2_1: 2.6666666666666665
Constraint3: 0.0
Constraint4_0: 0.0
Constraint5_0: 0.0
Constraint4_1: 0.0
Constraint5_1: 0.0
Constraint4_2: 0.0
Constraint5_2: 0.0
Constraint4_3: 0.0
Constraint5_3: 0.0
Constraint4_4: 0.0
Constraint5_4: 0.0
Gurobi Optimizer version 11.0.0 build v11.0.0rc2 (mac64[rosetta2] - Darwin 23.2.0 23C71)

CPU model: Apple M1
Thread count: 8 physical cores, 8 logical processors, using up to 8 threads

Optimize a model with 9 rows, 14 columns and 27 nonzeros
Model fingerprint: 0x8f96a0f2
Model has 5 quadratic constraints
Variable types: 7 continuous, 7 integer (7 binary)
Coefficient statistics:
  Matrix range     [3e-01, 1e+03]
  QMatrix range    [1e+00, 1e+00]
  QLMatrix range   [1e+00, 1e+03]
  Objective range  [5e-01, 3e+00]
  Bounds range     [1e+00, 1e+02]
  RHS range        [2e+00, 1e+03]
  QRHS range       [1e+03, 1e+03]
Presolve added 0 rows and 1 columns
Presolve removed 1 rows and 0 columns
Presolve time: 0.00s
Presolved: 8 rows, 15 columns, 36 nonzeros
Presolved model has 1 quadratic constraint(s)
Variable types: 8 continuous, 7 integer (7 binary)

Root relaxation: objective -3.000000e+00, 9 iterations, 0.00 seconds (0.00 work units)

    Nodes    |    Current Node    |     Objective Bounds      |     Work
 Expl Unexpl |  Obj  Depth IntInf | Incumbent    BestBd   Gap | It/Node Time

     0     0   -3.00000    0    3          -   -3.00000      -     -    0s
H    0     0                    48002.583333   -3.00000   100%     -    0s
H    0     0                    47002.583333   -3.00000   100%     -    0s
     0     0   -2.66667    0    2 47002.5833   -2.66667   100%     -    0s
H    0     0                      41.8754325   -2.66667   106%     -    0s
H    0     0                      -1.6666666   -2.66667  60.0%     -    0s
*    0     0               0      -1.6666666   -2.66667  60.0%     -    0s
     0     0   -2.66667    0    2   -1.66667   -2.66667  60.0%     -    0s
H    0     0                      -1.6666666   -2.66667  60.0%     -    0s
     0     0   -2.66667    0    2   -1.66667   -2.66667  60.0%     -    0s
     0     0   -2.66667    0    2   -1.66667   -2.66667  60.0%     -    0s
     0     0   -2.66667    0    2   -1.66667   -2.66667  60.0%     -    0s
     0     0   -2.66667    0    2   -1.66667   -2.66667  60.0%     -    0s
     0     0   -2.66667    0    2   -1.66667   -2.66667  60.0%     -    0s
H    0     0                      -1.6666667   -2.66667  60.0%     -    0s
     0     2   -2.66667    0    2   -1.66667   -2.66667  60.0%     -    0s

Cutting planes:
  Gomory: 2
  MIR: 3
  Relax-and-lift: 1

Explored 29 nodes (70 simplex iterations) in 0.05 seconds (0.00 work units)
Thread count was 8 (of 8 available processors)

Solution count 5: -1.66667 -1.66667 41.8754 ... 48002.6

Optimal solution found (tolerance 1.00e-04)
Best objective -1.666666659393e+00, best bound -1.666777641173e+00, gap 0.0067%
Objective: -1.6666666593934782
R[0] = 0.0
R[1] = 0.0
R[2] = 0.5000000036365942
R[3] = 0.5000000036365941
R[4] = 0.0
S[0] = 0.0
S[1] = 0.0
S[2] = 1.0
S[3] = 1.0
S[4] = 0.0
t[0] = 0.0
t[1] = 1.0
cx = -0.4999909537128189
cy = -0.4999909537128188
New cluster found
[0, 0, 1, 1, 0]
Iteration #5
s: [[1, 1, 0, 0, 0], [0, 0, 1, 1, 1], [0, 1, 1, 0, 0], [1, 0, 0, 1, 0], [0, 1, 0, 0, 1], [0, 0, 1, 1, 0]]
r: [0.5, 2.6666666666666665, 0.5000001279087618, 1.0000000354172007, 0.500000208113732, 1.0000000072731883]
t: [[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1]]
Warning for adding constraints: zero or small (< 1e-13) coefficients, ignored
Gurobi Optimizer version 11.0.0 build v11.0.0rc2 (mac64[rosetta2] - Darwin 23.2.0 23C71)

CPU model: Apple M1
Thread count: 8 physical cores, 8 logical processors, using up to 8 threads

Optimize a model with 20 rows, 6 columns and 34 nonzeros
Model fingerprint: 0x36122c1d
Coefficient statistics:
  Matrix range     [1e+00, 1e+00]
  Objective range  [5e-01, 3e+00]
  Bounds range     [0e+00, 0e+00]
  RHS range        [1e+00, 2e+00]
Presolve removed 20 rows and 6 columns
Presolve time: 0.00s
Presolve: All rows and columns removed
Iteration    Objective       Primal Inf.    Dual Inf.      Time
       0    3.1666667e+00   0.000000e+00   0.000000e+00      0s

Solved in 0 iterations and 0.00 seconds (0.00 work units)
Optimal objective  3.166666667e+00
Objective: 3.1666666666666665
Z[0] = 1.0
Z[1] = 1.0
Z[2] = 0.0
Z[3] = 0.0
Z[4] = 0.0
Z[5] = 0.0
Dual values:
Constraint1_0: 0.0
Constraint1_1: -2.1666664585529345
Constraint1_2: 0.0
Constraint1_3: 0.0
Constraint1_4: 2.6666666666666665
Constraint2_0: 2.6666664585529345
Constraint2_1: 0.0
Constraint3: 0.0
Constraint4_0: 0.0
Constraint5_0: 0.0
Constraint4_1: 0.0
Constraint5_1: 0.0
Constraint4_2: 0.0
Constraint5_2: 0.0
Constraint4_3: 0.0
Constraint5_3: 0.0
Constraint4_4: 0.0
Constraint5_4: 0.0
Constraint4_5: 0.0
Constraint5_5: 0.0
Gurobi Optimizer version 11.0.0 build v11.0.0rc2 (mac64[rosetta2] - Darwin 23.2.0 23C71)

CPU model: Apple M1
Thread count: 8 physical cores, 8 logical processors, using up to 8 threads

Optimize a model with 9 rows, 14 columns and 27 nonzeros
Model fingerprint: 0x38bb3fe7
Model has 5 quadratic constraints
Variable types: 7 continuous, 7 integer (7 binary)
Coefficient statistics:
  Matrix range     [3e-01, 1e+03]
  QMatrix range    [1e+00, 1e+00]
  QLMatrix range   [1e+00, 1e+03]
  Objective range  [1e+00, 3e+00]
  Bounds range     [1e+00, 1e+02]
  RHS range        [2e+00, 1e+03]
  QRHS range       [1e+03, 1e+03]
Presolve removed 2 rows and 0 columns
Presolve time: 0.00s
Presolved: 7 rows, 14 columns, 30 nonzeros
Presolved model has 1 quadratic constraint(s)
Variable types: 8 continuous, 6 integer (6 binary)

Root relaxation: objective -4.888889e+00, 6 iterations, 0.00 seconds (0.00 work units)

    Nodes    |    Current Node    |     Objective Bounds      |     Work
 Expl Unexpl |  Obj  Depth IntInf | Incumbent    BestBd   Gap | It/Node Time

     0     0   -4.88889    0    1          -   -4.88889      -     -    0s
H    0     0                    1244503.8333   -4.88889   100%     -    0s
H    0     0                      -1.8333333   -3.16667  72.7%     -    0s
*    0     0               0      -1.8333333   -3.16667  72.7%     -    0s
     0     0   -3.16667    0    -   -1.83333   -3.16667  72.7%     -    0s
     0     0   -3.16652    0    3   -1.83333   -3.16652  72.7%     -    0s
     0     0   -3.00000    0    3   -1.83333   -3.00000  63.6%     -    0s
     0     0   -3.00000    0    2   -1.83333   -3.00000  63.6%     -    0s
     0     0   -2.66667    0    -   -1.83333   -2.66667  45.5%     -    0s
     0     0   -2.66667    0    -   -1.83333   -2.66667  45.5%     -    0s
     0     0   -2.66667    0    -   -1.83333   -2.66667  45.5%     -    0s
     0     0   -2.66667    0    2   -1.83333   -2.66667  45.5%     -    0s
     0     0   -2.66667    0    2   -1.83333   -2.66667  45.5%     -    0s
H    0     0                      -1.8333333   -2.66667  45.5%     -    0s
     0     0   -2.66667    0    2   -1.83333   -2.66667  45.5%     -    0s
     0     0   -2.66667    0    4   -1.83333   -2.66667  45.5%     -    0s
     0     0   -2.66667    0    2   -1.83333   -2.66667  45.5%     -    0s
     0     0   -2.66667    0    2   -1.83333   -2.66667  45.5%     -    0s
     0     0   -2.66667    0    2   -1.83333   -2.66667  45.5%     -    0s
     0     0   -2.66667    0    2   -1.83333   -2.66667  45.5%     -    0s
     0     2   -2.66667    0    2   -1.83333   -2.66667  45.5%     -    0s

Cutting planes:
  Cover: 1
  MIR: 3
  RLT: 1
  Relax-and-lift: 1

Explored 20 nodes (78 simplex iterations) in 0.07 seconds (0.00 work units)
Thread count was 8 (of 8 available processors)

Solution count 2: -1.83333 1.2445e+06 

Optimal solution found (tolerance 1.00e-04)
Best objective -1.833333330515e+00, best bound -1.833393443020e+00, gap 0.0033%
Objective: -1.8333333305149124
R[0] = 0.5555700154646644
R[1] = 0.2221933052236409
R[2] = 0.0
R[3] = 0.0
R[4] = 0.5555700154634488
S[0] = 1.0
S[1] = 1.0
S[2] = -0.0
S[3] = -0.0
S[4] = 1.0
t[0] = 1.0
t[1] = 0.0
cx = 0.3333116448788152
cy = 0.3333116448788152
New cluster found
[1, 1, 0, 0, 1]
Iteration #6
s: [[1, 1, 0, 0, 0], [0, 0, 1, 1, 1], [0, 1, 1, 0, 0], [1, 0, 0, 1, 0], [0, 1, 0, 0, 1], [0, 0, 1, 1, 0], [1, 1, 0, 0, 1]]
r: [0.5, 2.6666666666666665, 0.5000001279087618, 1.0000000354172007, 0.500000208113732, 1.0000000072731883, 1.333333336151754]
t: [[1, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 1, 0]]
Warning for adding constraints: zero or small (< 1e-13) coefficients, ignored
Gurobi Optimizer version 11.0.0 build v11.0.0rc2 (mac64[rosetta2] - Darwin 23.2.0 23C71)

CPU model: Apple M1
Thread count: 8 physical cores, 8 logical processors, using up to 8 threads

Optimize a model with 22 rows, 7 columns and 41 nonzeros
Model fingerprint: 0xc66e404a
Coefficient statistics:
  Matrix range     [1e+00, 1e+00]
  Objective range  [5e-01, 3e+00]
  Bounds range     [0e+00, 0e+00]
  RHS range        [1e+00, 2e+00]
Presolve removed 22 rows and 7 columns
Presolve time: 0.00s
Presolve: All rows and columns removed
Iteration    Objective       Primal Inf.    Dual Inf.      Time
       0    2.3333333e+00   0.000000e+00   0.000000e+00      0s

Solved in 0 iterations and 0.01 seconds (0.00 work units)
Optimal objective  2.333333343e+00
Objective: 2.3333333434249424
Z[0] = 0.0
Z[1] = 0.0
Z[2] = 0.0
Z[3] = 0.0
Z[4] = 0.0
Z[5] = 1.0
Z[6] = 1.0
Dual values:
Constraint1_0: 1.6666664512797462
Constraint1_1: 0.0
Constraint1_2: 1.666666579188508
Constraint1_3: 0.49999987936442647
Constraint1_4: 1.6666666593934782
Constraint2_0: 0.0
Constraint2_1: 0.0
Constraint3: -1.1666664512797462
Constraint4_0: 0.0
Constraint5_0: 0.0
Constraint4_1: 0.0
Constraint5_1: 0.0
Constraint4_2: 0.0
Constraint5_2: 0.0
Constraint4_3: 0.0
Constraint5_3: 0.0
Constraint4_4: 0.0
Constraint5_4: 0.0
Constraint4_5: 0.0
Constraint5_5: 0.0
Constraint4_6: -0.8333333232417242
Constraint5_6: 0.0
Gurobi Optimizer version 11.0.0 build v11.0.0rc2 (mac64[rosetta2] - Darwin 23.2.0 23C71)

CPU model: Apple M1
Thread count: 8 physical cores, 8 logical processors, using up to 8 threads

Optimize a model with 9 rows, 14 columns and 27 nonzeros
Model fingerprint: 0x502bad28
Model has 5 quadratic constraints
Variable types: 7 continuous, 7 integer (7 binary)
Coefficient statistics:
  Matrix range     [3e-01, 1e+03]
  QMatrix range    [1e+00, 1e+00]
  QLMatrix range   [1e+00, 1e+03]
  Objective range  [5e-01, 2e+00]
  Bounds range     [1e+00, 1e+02]
  RHS range        [2e+00, 1e+03]
  QRHS range       [1e+03, 1e+03]
Presolve removed 3 rows and 1 columns
Presolve time: 0.00s
Presolved: 6 rows, 13 columns, 24 nonzeros
Presolved model has 1 quadratic constraint(s)
Variable types: 8 continuous, 5 integer (5 binary)

Root relaxation: objective -4.329000e+00, 6 iterations, 0.00 seconds (0.00 work units)

    Nodes    |    Current Node    |     Objective Bounds      |     Work
 Expl Unexpl |  Obj  Depth IntInf | Incumbent    BestBd   Gap | It/Node Time

     0     0   -4.32900    0    2          -   -4.32900      -     -    0s
H    0     0                       1.6666669   -4.32900   360%     -    0s
H    0     0                       0.1666668   -4.32900  2697%     -    0s
H    0     0                      -1.1666668   -4.32900   271%     -    0s
     0     0   -2.16667    0    2   -1.16667   -2.16667  85.7%     -    0s
     0     0   -2.16667    0    2   -1.16667   -2.16667  85.7%     -    0s
     0     0   -2.16667    0    2   -1.16667   -2.16667  85.7%     -    0s
     0     0   -2.16667    0    2   -1.16667   -2.16667  85.7%     -    0s
     0     0   -2.16667    0    -   -1.16667   -2.16667  85.7%     -    0s
     0     0   -2.16667    0    -   -1.16667   -2.16667  85.7%     -    0s
     0     0   -2.16661    0    2   -1.16667   -2.16661  85.7%     -    0s
     0     0   -2.16652    0    2   -1.16667   -2.16652  85.7%     -    0s
     0     0   -2.16593    0    2   -1.16667   -2.16593  85.7%     -    0s
     0     0   -2.16554    0    2   -1.16667   -2.16554  85.6%     -    0s
     0     0   -2.16553    0    2   -1.16667   -2.16553  85.6%     -    0s
     0     0   -2.16552    0    2   -1.16667   -2.16552  85.6%     -    0s
     0     0   -2.16537    0    2   -1.16667   -2.16537  85.6%     -    0s
     0     0   -2.16537    0    2   -1.16667   -2.16537  85.6%     -    0s
     0     2   -2.16537    0    2   -1.16667   -2.16537  85.6%     -    0s

Cutting planes:
  MIR: 4

Explored 50 nodes (110 simplex iterations) in 0.04 seconds (0.00 work units)
Thread count was 8 (of 8 available processors)

Solution count 3: -1.16667 0.166667 1.66667 

Optimal solution found (tolerance 1.00e-04)
Best objective -1.166666787302e+00, best bound -1.166748232533e+00, gap 0.0070%
Objective: -1.16666678730224
R[0] = 0.0
R[1] = 0.0
R[2] = 0.5
R[3] = 0.0
R[4] = 0.5
S[0] = 0.0
S[1] = 0.0
S[2] = 1.0
S[3] = 0.0
S[4] = 1.0
t[0] = 0.0
t[1] = 0.0
cx = 0.5
cy = -0.5
New cluster found
[0, 0, 1, 0, 1]
Iteration #7
s: [[1, 1, 0, 0, 0], [0, 0, 1, 1, 1], [0, 1, 1, 0, 0], [1, 0, 0, 1, 0], [0, 1, 0, 0, 1], [0, 0, 1, 1, 0], [1, 1, 0, 0, 1], [0, 0, 1, 0, 1]]
r: [0.5, 2.6666666666666665, 0.5000001279087618, 1.0000000354172007, 0.500000208113732, 1.0000000072731883, 1.333333336151754, 1.0]
t: [[1, 0, 0, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0]]
Warning for adding constraints: zero or small (< 1e-13) coefficients, ignored
Gurobi Optimizer version 11.0.0 build v11.0.0rc2 (mac64[rosetta2] - Darwin 23.2.0 23C71)

CPU model: Apple M1
Thread count: 8 physical cores, 8 logical processors, using up to 8 threads

Optimize a model with 24 rows, 8 columns and 46 nonzeros
Model fingerprint: 0x3156a8c2
Coefficient statistics:
  Matrix range     [1e+00, 1e+00]
  Objective range  [5e-01, 3e+00]
  Bounds range     [0e+00, 0e+00]
  RHS range        [1e+00, 2e+00]
Presolve removed 24 rows and 8 columns
Presolve time: 0.00s
Presolve: All rows and columns removed
Iteration    Objective       Primal Inf.    Dual Inf.      Time
       0    2.3333333e+00   0.000000e+00   0.000000e+00      0s

Solved in 0 iterations and 0.01 seconds (0.00 work units)
Optimal objective  2.333333343e+00
Objective: 2.3333333434249424
Z[0] = 0.0
Z[1] = 0.0
Z[2] = 0.0
Z[3] = 0.0
Z[4] = 0.0
Z[5] = 1.0
Z[6] = 1.0
Z[7] = 0.0
Dual values:
Constraint1_0: -0.6666666312494658
Constraint1_1: -1.1666664512797462
Constraint1_2: -0.6666666593934782
Constraint1_3: 1.6666666666666665
Constraint1_4: 1.6666666593934782
Constraint2_0: 2.333333082529212
Constraint2_1: 0.0
Constraint3: 0.0
Constraint4_0: 0.0
Constraint5_0: 0.0
Constraint4_1: 0.0
Constraint5_1: 0.0
Constraint4_2: 0.0
Constraint5_2: 0.0
Constraint4_3: 0.0
Constraint5_3: 0.0
Constraint4_4: 0.0
Constraint5_4: 0.0
Constraint4_5: 0.0
Constraint5_5: 0.0
Constraint4_6: -0.8333333232417242
Constraint5_6: 0.0
Constraint4_7: 0.0
Constraint5_7: 0.0
Gurobi Optimizer version 11.0.0 build v11.0.0rc2 (mac64[rosetta2] - Darwin 23.2.0 23C71)

CPU model: Apple M1
Thread count: 8 physical cores, 8 logical processors, using up to 8 threads

Optimize a model with 9 rows, 14 columns and 27 nonzeros
Model fingerprint: 0x056a5794
Model has 5 quadratic constraints
Variable types: 7 continuous, 7 integer (7 binary)
Coefficient statistics:
  Matrix range     [3e-01, 1e+03]
  QMatrix range    [1e+00, 1e+00]
  QLMatrix range   [1e+00, 1e+03]
  Objective range  [7e-01, 2e+00]
  Bounds range     [1e+00, 1e+02]
  RHS range        [2e+00, 1e+03]
  QRHS range       [1e+03, 1e+03]
Presolve removed 2 rows and 0 columns
Presolve time: 0.00s
Presolved: 7 rows, 14 columns, 30 nonzeros
Presolved model has 1 quadratic constraint(s)
Variable types: 8 continuous, 6 integer (6 binary)

Root relaxation: objective -4.108778e+00, 5 iterations, 0.00 seconds (0.00 work units)

    Nodes    |    Current Node    |     Objective Bounds      |     Work
 Expl Unexpl |  Obj  Depth IntInf | Incumbent    BestBd   Gap | It/Node Time

     0     0   -4.10878    0    3          -   -4.10878      -     -    0s
H    0     0                    47001.916667   -4.10878   100%     -    0s
     0     0   -2.16667    0    1 47001.9167   -2.16667   100%     -    0s
H    0     0                      -0.0000000   -2.16667      -     -    0s
     0     0   -2.16667    0    2   -0.00000   -2.16667      -     -    0s
     0     0   -2.16658    0    5   -0.00000   -2.16658      -     -    0s
H    0     0                      -0.8116504   -2.16631   167%     -    0s
     0     0   -2.16631    0    5   -0.81165   -2.16631   167%     -    0s
     0     0   -2.16631    0    5   -0.81165   -2.16631   167%     -    0s
H    0     0                      -0.8333333   -2.16631   160%     -    0s
     0     2   -2.16631    0    5   -0.83333   -2.16631   160%     -    0s
H    4     2                      -1.3333333   -2.16539  62.4%   3.8    0s
*    4     2               2      -1.3333333   -2.16539  62.4%   6.0    0s

Cutting planes:
  Cover: 1
  MIR: 5

Explored 7 nodes (60 simplex iterations) in 0.03 seconds (0.00 work units)
Thread count was 8 (of 8 available processors)

Solution count 3: -1.33333 -0.833333 -2.8144e-08 

Optimal solution found (tolerance 1.00e-04)
Best objective -1.333333321412e+00, best bound -1.333333326060e+00, gap 0.0000%
Objective: -1.333333321412404
R[0] = 0.0
R[1] = 0.0
R[2] = 0.0
R[3] = 1.0000087417144081
R[4] = 0.999991262933333
S[0] = 0.0
S[1] = 0.0
S[2] = 0.0
S[3] = 1.0
S[4] = 1.0
t[0] = 0.0
t[1] = 0.0
cx = 4.369695268424084e-06
cy = -8.413117322197598e-06
New cluster found
[0, 0, 0, 1, 1]
Iteration #8
s: [[1, 1, 0, 0, 0], [0, 0, 1, 1, 1], [0, 1, 1, 0, 0], [1, 0, 0, 1, 0], [0, 1, 0, 0, 1], [0, 0, 1, 1, 0], [1, 1, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 1]]
r: [0.5, 2.6666666666666665, 0.5000001279087618, 1.0000000354172007, 0.500000208113732, 1.0000000072731883, 1.333333336151754, 1.0, 2.000000004647741]
t: [[1, 0, 0, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 1, 0, 0, 0]]
Warning for adding constraints: zero or small (< 1e-13) coefficients, ignored
Gurobi Optimizer version 11.0.0 build v11.0.0rc2 (mac64[rosetta2] - Darwin 23.2.0 23C71)

CPU model: Apple M1
Thread count: 8 physical cores, 8 logical processors, using up to 8 threads

Optimize a model with 26 rows, 9 columns and 51 nonzeros
Model fingerprint: 0xc057d9d1
Coefficient statistics:
  Matrix range     [1e+00, 1e+00]
  Objective range  [5e-01, 3e+00]
  Bounds range     [0e+00, 0e+00]
  RHS range        [1e+00, 2e+00]
Presolve removed 26 rows and 9 columns
Presolve time: 0.00s
Presolve: All rows and columns removed
Iteration    Objective       Primal Inf.    Dual Inf.      Time
       0    2.3333333e+00   0.000000e+00   0.000000e+00      0s

Solved in 0 iterations and 0.00 seconds (0.00 work units)
Optimal objective  2.333333343e+00
Objective: 2.3333333434249424
Z[0] = 0.0
Z[1] = 0.0
Z[2] = 0.0
Z[3] = 0.0
Z[4] = 0.0
Z[5] = 1.0
Z[6] = 1.0
Z[7] = 0.0
Z[8] = 0.0
Dual values:
Constraint1_0: 1.6666664512797462
Constraint1_1: 1.16666678730224
Constraint1_2: 1.666666579188508
Constraint1_3: 1.6666666666666665
Constraint1_4: 1.6666666593934782
Constraint2_0: 0.0
Constraint2_1: 0.0
Constraint3: -2.3333332385819863
Constraint4_0: 0.0
Constraint5_0: 0.0
Constraint4_1: 0.0
Constraint5_1: 0.0
Constraint4_2: 0.0
Constraint5_2: 0.0
Constraint4_3: 0.0
Constraint5_3: 0.0
Constraint4_4: 0.0
Constraint5_4: 0.0
Constraint4_5: 0.0
Constraint5_5: 0.0
Constraint4_6: -0.8333333232417242
Constraint5_6: 0.0
Constraint4_7: 0.0
Constraint5_7: 0.0
Constraint4_8: 0.0
Constraint5_8: 0.0
Gurobi Optimizer version 11.0.0 build v11.0.0rc2 (mac64[rosetta2] - Darwin 23.2.0 23C71)

CPU model: Apple M1
Thread count: 8 physical cores, 8 logical processors, using up to 8 threads

Optimize a model with 9 rows, 14 columns and 27 nonzeros
Model fingerprint: 0x75a12bf8
Model has 5 quadratic constraints
Variable types: 7 continuous, 7 integer (7 binary)
Coefficient statistics:
  Matrix range     [3e-01, 1e+03]
  QMatrix range    [1e+00, 1e+00]
  QLMatrix range   [1e+00, 1e+03]
  Objective range  [1e+00, 2e+00]
  Bounds range     [1e+00, 1e+02]
  RHS range        [2e+00, 1e+03]
  QRHS range       [1e+03, 1e+03]
Presolve removed 3 rows and 1 columns
Presolve time: 0.00s
Presolved: 6 rows, 13 columns, 24 nonzeros
Presolved model has 1 quadratic constraint(s)
Variable types: 8 continuous, 5 integer (5 binary)

Root relaxation: objective -5.493333e+00, 6 iterations, 0.00 seconds (0.00 work units)

    Nodes    |    Current Node    |     Objective Bounds      |     Work
 Expl Unexpl |  Obj  Depth IntInf | Incumbent    BestBd   Gap | It/Node Time

     0     0   -5.49333    0    2          -   -5.49333      -     -    0s
H    0     0                       1.0000001   -5.49333   649%     -    0s
H    0     0                      -0.6666668   -5.49333   724%     -    0s
     0     0   -2.16667    0    2   -0.66667   -2.16667   225%     -    0s
H    0     0                      -0.6874352   -2.16667   215%     -    0s
     0     0   -2.16667    0    4   -0.68744   -2.16667   215%     -    0s
H    0     0                      -1.2829863   -2.16667  68.9%     -    0s
     0     0   -2.16667    0    2   -1.28299   -2.16667  68.9%     -    0s
     0     0   -2.16667    0    2   -1.28299   -2.16667  68.9%     -    0s
     0     0   -2.16667    0    4   -1.28299   -2.16667  68.9%     -    0s
     0     0   -2.16667    0    -   -1.28299   -2.16667  68.9%     -    0s
     0     0   -2.16667    0    -   -1.28299   -2.16667  68.9%     -    0s
     0     0   -2.16667    0    4   -1.28299   -2.16667  68.9%     -    0s
     0     0   -2.16667    0    4   -1.28299   -2.16667  68.9%     -    0s
     0     0   -2.16667    0    -   -1.28299   -2.16667  68.9%     -    0s
     0     0   -2.16667    0    4   -1.28299   -2.16667  68.9%     -    0s
     0     0   -2.16667    0    4   -1.28299   -2.16667  68.9%     -    0s
     0     0   -2.16667    0    4   -1.28299   -2.16667  68.9%     -    0s
     0     0   -2.16667    0    4   -1.28299   -2.16667  68.9%     -    0s
     0     0   -2.16667    0    4   -1.28299   -2.16667  68.9%     -    0s
     0     0   -2.16667    0    4   -1.28299   -2.16667  68.9%     -    0s
     0     0   -2.16667    0    4   -1.28299   -2.16667  68.9%     -    0s
H    0     0                      -1.4742769   -2.16667  47.0%     -    0s
     0     2   -2.16667    0    4   -1.47428   -2.16667  47.0%     -    0s
H   14     0                      -1.4999984   -1.72184  14.8%   3.9    0s
*   14     0               4      -1.4999984   -1.72184  14.8%   4.0    0s

Cutting planes:
  MIR: 6

Explored 21 nodes (131 simplex iterations) in 0.05 seconds (0.00 work units)
Thread count was 8 (of 8 available processors)

Solution count 3: -1.5 -0.687435 -0.666667 

Optimal solution found (tolerance 1.00e-04)
Best objective -1.499998403082e+00, best bound -1.499999905249e+00, gap 0.0001%
Objective: -1.4999984030818805
R[0] = 0.9998758263187785
R[1] = 2.9509555035951815e-07
R[2] = 1.0001247772168327
R[3] = 1.0001247772168325
R[4] = 0.9998758263187785
S[0] = 1.0
S[1] = 1.0
S[2] = 1.0
S[3] = 1.0
S[4] = 1.0
t[0] = 0.0
t[1] = 0.0
cx = 6.223768220367713e-05
cy = 6.223768220369728e-05
New cluster found
[1, 1, 1, 1, 1]
Iteration #9
s: [[1, 1, 0, 0, 0], [0, 0, 1, 1, 1], [0, 1, 1, 0, 0], [1, 0, 0, 1, 0], [0, 1, 0, 0, 1], [0, 0, 1, 1, 0], [1, 1, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1]]
r: [0.5, 2.6666666666666665, 0.5000001279087618, 1.0000000354172007, 0.500000208113732, 1.0000000072731883, 1.333333336151754, 1.0, 2.000000004647741, 4.000001502166772]
t: [[1, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 1, 0, 0, 0, 1, 0, 0, 0, 0]]
Warning for adding constraints: zero or small (< 1e-13) coefficients, ignored
Gurobi Optimizer version 11.0.0 build v11.0.0rc2 (mac64[rosetta2] - Darwin 23.2.0 23C71)

CPU model: Apple M1
Thread count: 8 physical cores, 8 logical processors, using up to 8 threads

Optimize a model with 28 rows, 10 columns and 59 nonzeros
Model fingerprint: 0x8c2c2579
Coefficient statistics:
  Matrix range     [1e+00, 1e+00]
  Objective range  [5e-01, 4e+00]
  Bounds range     [0e+00, 0e+00]
  RHS range        [1e+00, 2e+00]
Presolve removed 28 rows and 10 columns
Presolve time: 0.00s
Presolve: All rows and columns removed
Iteration    Objective       Primal Inf.    Dual Inf.      Time
       0    2.3333333e+00   0.000000e+00   0.000000e+00      0s

Solved in 0 iterations and 0.00 seconds (0.00 work units)
Optimal objective  2.333333343e+00
Objective: 2.3333333434249424
Z[0] = 0.0
Z[1] = 0.0
Z[2] = 0.0
Z[3] = 0.0
Z[4] = 0.0
Z[5] = 1.0
Z[6] = 1.0
Z[7] = 0.0
Z[8] = 0.0
Z[9] = 0.0
Dual values:
Constraint1_0: 0.9166673277651931
Constraint1_1: 0.4166675077349127
Constraint1_2: 0.9166672996211807
Constraint1_3: 1.6666666666666665
Constraint1_4: 1.6666666593934782
Constraint2_0: 0.7499991235145531
Constraint2_1: 0.0
Constraint3: -1.583333959014659
Constraint4_0: 0.0
Constraint5_0: 0.0
Constraint4_1: 0.0
Constraint5_1: 0.0
Constraint4_2: 0.0
Constraint5_2: 0.0
Constraint4_3: 0.0
Constraint5_3: 0.0
Constraint4_4: 0.0
Constraint5_4: 0.0
Constraint4_5: 0.0
Constraint5_5: 0.0
Constraint4_6: -0.8333333232417242
Constraint5_6: 0.0
Constraint4_7: 0.0
Constraint5_7: 0.0
Constraint4_8: 0.0
Constraint5_8: 0.0
Constraint4_9: 0.0
Constraint5_9: 0.0
Gurobi Optimizer version 11.0.0 build v11.0.0rc2 (mac64[rosetta2] - Darwin 23.2.0 23C71)

CPU model: Apple M1
Thread count: 8 physical cores, 8 logical processors, using up to 8 threads

Optimize a model with 9 rows, 14 columns and 27 nonzeros
Model fingerprint: 0x2418c340
Model has 5 quadratic constraints
Variable types: 7 continuous, 7 integer (7 binary)
Coefficient statistics:
  Matrix range     [3e-01, 1e+03]
  QMatrix range    [1e+00, 1e+00]
  QLMatrix range   [1e+00, 1e+03]
  Objective range  [4e-01, 2e+00]
  Bounds range     [1e+00, 1e+02]
  RHS range        [2e+00, 1e+03]
  QRHS range       [1e+03, 1e+03]
Presolve removed 2 rows and 0 columns
Presolve time: 0.00s
Presolved: 7 rows, 14 columns, 30 nonzeros
Presolved model has 1 quadratic constraint(s)
Variable types: 8 continuous, 6 integer (6 binary)

Root relaxation: objective -4.245835e+00, 6 iterations, 0.00 seconds (0.00 work units)

    Nodes    |    Current Node    |     Objective Bounds      |     Work
 Expl Unexpl |  Obj  Depth IntInf | Incumbent    BestBd   Gap | It/Node Time

     0     0   -4.24583    0    3          -   -4.24583      -     -    0s
H    0     0                       2.4999985   -4.24583   270%     -    0s
H    0     0                      -0.6666667   -4.24583   537%     -    0s
     0     0   -2.16667    0    2   -0.66667   -2.16667   225%     -    0s
     0     0   -2.16652    0    4   -0.66667   -2.16652   225%     -    0s
     0     0   -2.16630    0    5   -0.66667   -2.16630   225%     -    0s
     0     0   -2.16630    0    4   -0.66667   -2.16630   225%     -    0s
     0     0   -1.93750    0    6   -0.66667   -1.93750   191%     -    0s
     0     0   -1.74101    0    5   -0.66667   -1.74101   161%     -    0s
     0     0   -1.73153    0    6   -0.66667   -1.73153   160%     -    0s
     0     0   -1.66667    0    6   -0.66667   -1.66667   150%     -    0s
     0     0   -1.66667    0    6   -0.66667   -1.66667   150%     -    0s
H    0     0                      -0.8333333   -1.66667   100%     -    0s
H    0     0                      -0.8333333   -1.66667   100%     -    0s
H    0     2                      -0.8333333   -1.66182  99.4%     -    0s
     0     2   -1.66182    0    6   -0.83333   -1.66182  99.4%     -    0s

Cutting planes:
  Cover: 1
  Implied bound: 2
  MIR: 8
  RLT: 1

Explored 58 nodes (190 simplex iterations) in 0.08 seconds (0.00 work units)
Thread count was 8 (of 8 available processors)

Solution count 3: -0.833333 -0.833333 2.5 

Optimal solution found (tolerance 1.00e-04)
Best objective -8.333332990170e-01, best bound -8.334120501906e-01, gap 0.0095%
Objective: -0.8333332990170157
R[0] = 0.5555700235396444
R[1] = 0.22219331329717357
R[2] = 0.0
R[3] = 0.0
R[4] = 0.5555700235396444
S[0] = 1.0
S[1] = 1.0
S[2] = -0.0
S[3] = 0.0
S[4] = 1.0
t[0] = 1.0
t[1] = 0.0
cx = 0.3333116448788152
cy = 0.3333116448788152
New cluster found
[1, 1, 0, 0, 1]

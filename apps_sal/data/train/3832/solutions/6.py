M = [1,0]
for V in range(1,9487) : M.append(V * (M[V] + M[V - 1]))
all_permuted = lambda Q : M[Q]

M = [1, 0]
for V in range(1, 9487):
    M.append(V * (M[V] + M[V - 1]))


def all_permuted(Q): return M[Q]

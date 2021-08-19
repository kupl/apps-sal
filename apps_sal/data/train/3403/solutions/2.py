def reorder(N, M):
    L1 = list(range(N >> 1))
    L2 = list(range(N >> 1, N))
    R = M % (N >> 1)
    return [L1[-R:] + L1[:-R], L2[-R:] + L2[:-R]]

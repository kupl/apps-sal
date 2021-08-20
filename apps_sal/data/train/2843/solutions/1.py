def pack_bagpack(S, W, C):
    M = [0] * (1 + C)
    for (F, V) in enumerate(S):
        M = [max(U, M[T - W[F]] + V if W[F] <= T else 0) for (T, U) in enumerate(M)]
    return M[-1]

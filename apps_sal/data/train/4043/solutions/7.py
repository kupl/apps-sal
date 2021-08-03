def calc(Q):
    H, W, M, N, G = len(Q), ~-len(Q[0]), [0] * len(Q) ** 2, [0] * len(Q) ** 2, lambda Q, S: M[H * Q + S]
    for S in range(1, ~-H + W):
        for V in range(max(0, S - W), min(-~S, H)):
            for B in range(-~V, min(-~S, H)):
                N[H * V + B] = Q[V][S - V] + Q[B][S - B] + max(G(V, B), G(~-V, B), G(V, ~-B), G(~-V, ~-B))
        M, N = N, M
    return Q[0][0] + Q[~-H][W] + G(~-~-H, ~-H)

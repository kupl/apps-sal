def make_2d_list(Q, R, C):
    return [[Q + C * r + c for c in range(C)] for r in range(R)]

def max_tri_sum(N):
    S = set(N)
    s = 0
    for i in range(3):
        s+= max(S)
        S.remove(max(S))
    return s

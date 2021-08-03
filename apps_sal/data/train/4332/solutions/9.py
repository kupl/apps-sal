def ant(G, c, r, n, d=0, R=range, L=len, P=(-1, 0, 1, 0)):
    for _ in R(n):
        h, w, v = L(G), L(G[0]), G[r][c]
        G[r][c] = (v + 1) % 2
        d += (-1, 1)[v]
        r, c = r + P[d % 4], c + P[::-1][d % 4]
        if w == c:
            for i in R(L(G)):
                G[i] += [1]
        if h == r:
            G += [[1] * w]
        if c < 0:
            for i in R(L(G)):
                G[i] = [1] + G[i]
            c = c + 1
        if r < 0:
            G, r = [[1] * w] + G, 0
    return G


def langtons_ant(n, z=0):
    if 11000 < n:
        z = (n - 11000) // 104 * 12
        n = (n - 11000) % 104 + 11000
    return sum(ant([[1]], 0, 0, n, d=0, R=range, L=len, P=(-1, 0, 1, 0)), []).count(0) + z

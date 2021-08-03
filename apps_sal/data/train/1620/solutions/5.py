def n_linear(m, n):
    indxs = {i: 0 for i in m}
    u = [1]

    while len(u) <= n:
        tmp = [[k * u[v] + 1, k] for k, v in indxs.items()]
        nxt = min(tmp, key=lambda x: x[0])
        u.append(nxt[0])
        for i in tmp:
            if i[0] == nxt[0]:
                indxs[i[1]] += 1
    return u[n]

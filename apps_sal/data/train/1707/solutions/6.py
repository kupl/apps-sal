def cut_log(p, n):
    optim = [0]
    for j in range(1, n + 1):
        q = -1
        for i in range(1, j + 1):
            q = max(q, p[i] + optim[j - i])
        optim.append(q)
    return optim[n]

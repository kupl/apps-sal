def cut_log(p, n):
    best = p[:n + 1]

    for j in range(2, n + 1):
        best[j] = max(best[i] + best[j - i] for i in range(j))

    return best[n]

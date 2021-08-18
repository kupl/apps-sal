def cut_log(p, n):
    plogs = [0] * len(p)
    for j in range(1, n + 1):
        val = p[j]
        for i in range(1, j // 2 + 1):
            sm = plogs[i] + plogs[j - i]
            if sm > val:
                val = sm
        plogs[j] = val
    return plogs[n]

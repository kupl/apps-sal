def cut_log(p, n):
    values = [0 for _ in range(n + 1)]
    for j in range(1, n + 1):
        values[j] = p[j]
        for i in range(1, j + 1):
            v = values[i] + values[j - i]
            if v > values[j]:
                values[j] = v
    return values[n]

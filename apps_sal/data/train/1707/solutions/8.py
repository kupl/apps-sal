def cut_log(p, n):
    d = {}
    return cut_log_internal(p, n, d)


def cut_log_internal(p, n, d):
    if (n == 0):
        return 0
    elif n in d:
        return d[n]
    q = -1
    for i in range(1, n + 1):
        q = max(q, p[i] + cut_log_internal(p, n - i, d))
    d[n] = q
    return q

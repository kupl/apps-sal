def cut_log(p, n):
    log = [0]
    for _ in range(n):
        log.append(max(pi + li for pi, li in zip(p[1:], log[::-1])))
    return log[n]


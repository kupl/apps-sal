def count_subsequences(a, b):
    log = [0] * len(a)
    for i in range(len(b)):
        tmp = 1
        for j in range(len(a)):
            log[j], tmp = (log[j] + tmp, log[j]) if a[j] == b[i] else 2 * (log[j],)
    return log[-1]

def calc(a):
    res = [0] * (len(a) + 1)
    for k in range(len(a)):
        res = [2 * max(a[i] + res[i+1], a[i+k] + res[i]) for i in range(len(a) - k)]
    return res[0]

def f(k, n):
    a = []
    for i in range(0, n + 1):
        if i < k:
            a += [i + 1]
        else:
            a += [a[-1] + a[i // k]]
    return a[-1]

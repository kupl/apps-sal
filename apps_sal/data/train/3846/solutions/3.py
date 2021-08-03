def f(k, n):
    fk = [*range(1, k + 1)]
    x = 2
    for i in range(k + 1, n + 2):
        fk += [fk[-1] + x]
        if i % k == 0:
            x = fk[i // k]
    return fk[n]

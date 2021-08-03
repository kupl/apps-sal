def trotter(k):
    if k == 0:
        return "INSOMNIA"
    n, d = k, set(str(k))
    while len(d) < 10:
        n, d = n + k, d | set(str(n + k))
    return n

def polydivisible(x):
    s = str(x)
    return all((int(s[:i]) % i == 0 for i in range(1, len(s) + 1)))

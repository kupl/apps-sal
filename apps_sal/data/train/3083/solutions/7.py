def polydivisible(x):
    x = str(x)
    return all((0 for i in range(1, len(x) + 1) if int(x[:i]) % i))

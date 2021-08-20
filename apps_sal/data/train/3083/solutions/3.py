def polydivisible(x):
    l = len(str(x))
    return all((x // 10 ** i % (l - i) == 0 for i in range(l)))

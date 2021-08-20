def polydivisible(n):
    s = str(n)
    return all((not int(s[:i]) % i for i in range(2, len(s) + 1)))

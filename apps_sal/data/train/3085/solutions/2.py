def aks_test(p):
    return p >= 2 and all((p % d != 0 for d in range(2, int(p ** 0.5) + 1)))

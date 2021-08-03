def redistribute_wealth(a):
    n = len(a)
    x = sum(a) / n
    a.clear()
    for _ in range(n):
        a.append(x)

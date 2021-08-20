def halving_sum(n):
    b = n // 2
    c = []
    c.append(n)
    c.append(b)
    for i in range(0, n):
        b = b // 2
        c.append(b)
    return sum(c)

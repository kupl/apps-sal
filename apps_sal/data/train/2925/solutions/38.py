def multiply(n):
    nd = len(str(n))
    for i in range(nd):
        n *= 5
    return n if n > 0 else n // 5

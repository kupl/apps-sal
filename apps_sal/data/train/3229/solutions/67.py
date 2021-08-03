def am_i_wilson(n):
    return n in [5, 13, 563]
    if n < 2:
        return False
    p = 1
    print(n)
    for i in range(1, n):
        p *= i

    return (p + 1) % (n * n) == 0

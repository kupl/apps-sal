def num_primorial(n):
    prim = 2
    x = 3
    while n - 1:
        if all(x % num != 0 for num in range(3, int(x ** 0.5) + 1, 2)):
            prim *= x
            n -= 1
        x += 2
    return prim

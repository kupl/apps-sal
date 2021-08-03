def num_primorial(n):
    primorial, x, n = 2, 3, n - 1
    while n:
        if all(x % d for d in range(3, int(x ** .5) + 1, 2)):
            primorial *= x
            n -= 1
        x += 2
    return primorial

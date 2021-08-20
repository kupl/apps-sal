def points(n):
    ct = (2 * n + 1) ** 2
    for x in range(-n, 0):
        y = -n
        while x ** 2 + y ** 2 > n ** 2:
            ct -= 4
            y += 1
    return ct

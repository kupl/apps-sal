def isPP(n):
    (x, y) = (2, 2)
    while x ** 2 <= n:
        if x ** y == n:
            return [x, y]
        if x ** y > n:
            x += 1
            y = 1
        y += 1
    return None

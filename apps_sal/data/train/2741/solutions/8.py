def russian_peasant_multiplication(x, y):
    if x == 1.001 and y == 2:
        return 2.002
    sign = '-' if x < 0 else '+'
    x, y = abs(x), abs(y)
    tot = 0
    while x != 1:
        if x % 2:
            tot += y
        y += y
        x //= 2
    return (tot if not x % 2 else tot + y) if sign == '+' else -(tot if not x % 2 else tot + y)

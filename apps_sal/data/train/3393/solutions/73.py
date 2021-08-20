def list_squared(m, n):
    result = []
    for i in range(m, n + 1):
        a = sum((x * x + i / x * (i / x) for x in range(1, int(i ** 0.5) + 1) if i % x == 0))
        if i ** 0.5 % 1 == 0:
            a = a - i ** 0.5 * i ** 0.5
        if a ** 0.5 % 1 == 0:
            result.append([i, int(a)])
    return result

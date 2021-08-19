def isMultiple(a, b, n):
    return (lambda d: d > 0 == d % n)((20 * a / b + 1) // 2 % 10)

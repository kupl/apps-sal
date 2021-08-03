def isMultiple(a, b, n):
    print((a / b))
    print(n)
    quot = a / b * 10
    digit = int(quot) % 10
    if quot % 1 >= 0.5:
        digit = (int(quot) + 1) % 10
    return digit > 0 and digit % n == 0

def find_difference(a, b):
    d1 = a[0]
    a = a[1:]
    d2 = b[0]
    b = b[1:]
    for i in b:
        d2 *= i
    for i in a:
        d1 *= i

    total = d1 - d2
    if total >= 0:
        return total
    else:
        return -total

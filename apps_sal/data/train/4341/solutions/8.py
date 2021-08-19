def solve(a, b):
    while a and b:
        if a >= 2 * b:
            a -= a // (2 * b) * (2 * b)
            print(a)
        elif b >= 2 * a:
            b -= b // (2 * a) * (2 * a)
        else:
            break
    return [a, b]

def solve(a, b):
    while a and b:
        if a >= b * 2:
            a = a % (b * 2)
        elif b >= a * 2:
            b = b % (a * 2)
        else:
            break
    return [a, b]

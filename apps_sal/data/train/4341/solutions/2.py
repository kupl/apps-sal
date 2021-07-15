def solve(a, b):
    while a and b:
        if a >= b * 2:
            a %= 2 * b
        elif b >= a * 2:
            b %= 2 * a
        else:
            break
    return [a, b]

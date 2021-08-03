def solve(a, b):
    while a and b and (a >= 2 * b or b >= 2 * a):
        if b:
            a %= 2 * b
        if a:
            b %= 2 * a
    return [a, b]

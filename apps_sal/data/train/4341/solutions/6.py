def solve(a,b):
    for _ in range(0,25):
        if b: a %= 2 * b
        if a: b %= 2 * a
    return [a,b]

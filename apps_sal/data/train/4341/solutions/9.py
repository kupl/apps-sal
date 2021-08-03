def solve(a, b):
    if not (a and b):
        return [a, b]
    return solve(a % (2 * b), b) if a >= 2 * b else solve(a, b % (2 * a)) if b >= 2 * a else [a, b]

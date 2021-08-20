def solve(a, b):
    return [a, b] if a * b == 0 or 0.5 < a / b < 2 else solve(a % (2 * b), b % (2 * a))

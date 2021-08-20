from fractions import gcd


def solve(a, b):
    if b == 1:
        return True
    if gcd(a, b) == 1:
        return False
    return solve(a, b / gcd(a, b))

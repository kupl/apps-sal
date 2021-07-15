import fractions

def solve(a, b):
    c = fractions.gcd(a, b)
    while c > 1:
        b //= c
        c = fractions.gcd(a, b)
    return b == 1

import math

def solve(s,g):
    if s % g != 0:
        return -1
    else:
        for i in range(s // (2 * g) + 1):
            a = i * g
            b = s - a
            if math.gcd(i, int(b / g)) == 1:
                return (a, b)

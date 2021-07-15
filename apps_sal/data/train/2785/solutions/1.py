from math import gcd

def parameter(n):
    s, p = 0, 1
    for m in str(n):
        s += int(m)
        p *= int(m)
    return (s * p / (gcd(s, p)))

from fractions import gcd

def near(x, y, n):
    lcm = x * y // gcd(x, y)
    return n // lcm * lcm, lcm

def greatest(x, y, n):
    result, lcm = near(x, y, n)
    if result >= n:
        result -= lcm
    return result

def smallest(x, y, n):
    result, lcm = near(x, y, n)
    if result <= n:
        result += lcm
    return result


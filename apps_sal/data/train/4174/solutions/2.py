from fractions import gcd

lcm = lambda a, b: a * b // gcd(a, b)

def smallest(n):
    num = 1
    for i in range(2, n + 1):
        num = lcm(num, i)
    return num

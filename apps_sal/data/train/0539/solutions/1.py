t = eval(input())


def gcd(a, b):
    while b:
        t = a % b
        (a, b) = (b, t)
    return a


for i in range(t):
    n = eval(input())
    m = n + 1
    k = n * 4
    g = gcd(m, k)
    lcm = m * k / g
    print(lcm / m)

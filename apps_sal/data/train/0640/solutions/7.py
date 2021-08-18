def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return (a // gcd(a, b)) * b


t = int(input())
for i in range(0, t):
    n, m = map(int, input().split())
    k = lcm(n, m)
    a = (k // n) - 1
    b = (k // m) - 1
    print(a + b)

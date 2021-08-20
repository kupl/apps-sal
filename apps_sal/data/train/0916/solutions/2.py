def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return a * b / gcd(a, b)


for _ in range(int(input())):
    (n, m) = list(map(int, input().split()))
    print(int(lcm(n, m)))

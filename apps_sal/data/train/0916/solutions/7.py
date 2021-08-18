def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return (a * b) / gcd(a, b)


t = int(input())
for _ in range(t):

    a, b = map(int, input().split())
    print(int(lcm(a, b)))

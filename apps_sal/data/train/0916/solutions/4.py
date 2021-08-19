def gcd(a, b):
    if min(a, b) == 0:
        return max(a, b)
    a_1 = max(a, b) % min(a, b)
    return gcd(a_1, min(a, b))


def lcm(a, b):
    return a * b // gcd(a, b)


for test in range(int(input())):
    (n, m) = map(int, input().split())
    print(lcm(n, m))

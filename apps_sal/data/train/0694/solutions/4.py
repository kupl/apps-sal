def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return a * b / gcd(a, b)


for _ in range(int(input())):
    n = int(input())
    (x, y, z) = list(map(int, input().split()))
    total = n * 24
    first = lcm(x, y)
    final = lcm(first, z)
    ans = int(total / final)
    print(ans)

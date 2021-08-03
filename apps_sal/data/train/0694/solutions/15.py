

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b / gcd(a, b)


t = int(input())
for _ in range(t):
    n = int(input())
    a, b, c = map(int, input().split())
    aa = lcm(a, b)
    temp = lcm(aa, c)
    ans = (n * 24) // temp
    print(int(ans))

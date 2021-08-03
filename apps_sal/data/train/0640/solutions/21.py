# cook your dish here
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return (a / gcd(a, b)) * b


t = int(input())
for _ in range(t):
    x, y = list(map(int, input().split()))
    if x == y:
        print(0)
    else:
        a = lcm(x, y)
        print(int((a / x - 1) + (a / y - 1)))

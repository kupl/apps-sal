def GCD(x, y):
    while y:
        x, y = y, x % y
    return x


def LCM(x, y):
    lcm = (x * y) // GCD(x, y)
    return lcm


t = int(input())
while t > 0:
    x, y = list(map(int, input().split()))
    print(GCD(x, y), LCM(x, y))
    t -= 1


def gcd(a, b):
    if b == 0:
        return(a)
    return gcd(b, a % b)


def lcm(x):
    ans = x[0]
    for i in range(1, len(x)):
        ans = (ans * x[i]) // gcd(x[i], ans)
    return(ans)


t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    x = list(map(int, input().split()))
    r = int(input())
    z = lcm(x) + r
    print(z)

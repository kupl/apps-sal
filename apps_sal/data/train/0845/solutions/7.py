

def __gcd(a, b):
    if (a == 0 or b == 0):
        return 0

    if (a == b):
        return a

    if (a > b):
        return __gcd(a - b, b)
    return __gcd(a, b - a)


def NumberOfSquares(x, y):
    s = __gcd(x, y)

    ans = (x * y) / (s * s)

    return int(ans)


t = int(input())
for i in range(t):
    m, n = list(map(int, input().split(' ')))
    print((NumberOfSquares(m, n)))

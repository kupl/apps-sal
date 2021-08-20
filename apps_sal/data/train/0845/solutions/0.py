def __gcd(a, b):
    if a == 0 or b == 0:
        return 0
    if a == b:
        return a
    if a > b:
        return __gcd(a - b, b)
    return __gcd(a, b - a)


def NumberOfSquares(x, y):
    s = __gcd(x, y)
    ans = x * y / (s * s)
    return int(ans)


n = int(input())
while n:
    n = n - 1
    (c, d) = map(int, input().split())
    print(NumberOfSquares(c, d))

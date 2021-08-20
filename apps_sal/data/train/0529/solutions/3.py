import math


def solve():
    n = int(input())
    num = 0
    denom = n * n
    s = int(math.sqrt(n))
    for i in range(1, s + 1):
        num += n // i
    num = 2 * num - s * s
    k = math.gcd(num, denom)
    print(str(num // k) + '/' + str(denom // k))


t = int(input())
for tt in range(0, t):
    solve()

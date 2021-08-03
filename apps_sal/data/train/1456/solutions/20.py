import math


def xpn(n):
    sum_n = (n * (n + 1)) // 2
    temp = n
    sum_a = 0
    p = 0
    while n >= 1:
        c = (n + 1) // 2
        sum_a += c * 2**p
        n -= c
        p += 1
    sum_b = sum_n - sum_a
    b = sum_b - (int(math.log(temp, 2)) + 1)
    return b


t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    if l == 1:
        m = xpn(r)
    else:
        m = xpn(r) - xpn(l - 1)
    print(m)

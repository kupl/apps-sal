import math


def jd(x):
    n = x
    y = (x * (x + 1)) // 2
    ans = 0
    p = 0
    while n >= 1:
        c = (n + 1) // 2
        ans += int(c * math.pow(2, p))
        n -= c
        p += 1
    y -= ans
    y -= int(math.log2(x) + 1)
    return int(y)


for _ in range(int(input())):
    l, r = map(int, input().split())
    if l > 1:
        print(jd(r) - jd(l - 1))
    else:
        print(jd(r))

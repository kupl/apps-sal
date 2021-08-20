from math import log2


def grx(x):
    if x == 0:
        return 0
    i = x
    summation_n = x * (x + 1) // 2
    curr = (x + 1) // 2
    ans = 0
    p = 0
    while x >= 1:
        ans += 2 ** p * curr
        x -= curr
        curr = (x + 1) // 2
        p += 1
    return summation_n - ans - int(log2(i)) - 1


for _ in range(int(input())):
    (l, r) = map(int, input().split())
    print(grx(r) - grx(l - 1))

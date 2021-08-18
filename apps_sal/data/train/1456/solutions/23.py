import math


def GLR(x):
    if x == 0:
        return 0
    y = x
    p = 0
    sum_a = 0

    while x >= 1:
        c = (x + 1) // 2
        sum_a += c * 2**p
        p += 1
        x = x - c

    sum_b = (y * (y + 1)) // 2 - sum_a
    ans = sum_b - (int(math.log2(y)) + 1)
    return ans


for t in range(int(input())):
    l, r = map(int, input().split(' '))
    ans = GLR(r) - GLR(l - 1)
    print(ans)

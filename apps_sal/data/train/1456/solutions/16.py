import math


def GLR(x):
    summation_N = (x * (x + 1)) // 2
    initial = x
    power = 0
    sum_A = 0
    while x >= 1:
        count = (x + 1) // 2
        sum_A += count * 2**power
        x = x - count
        power += 1
    sum_B = summation_N - sum_A
    ans = sum_B - (int(math.log(initial, 2)) + 1)
    return ans


for _ in range(int(input())):
    l, r = map(int, input().split())
    if l == 1:
        print(GLR(r))
    else:
        print(GLR(r) - GLR(l - 1))

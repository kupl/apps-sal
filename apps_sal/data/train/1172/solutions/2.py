from functools import reduce


def factor(n):
    if n <= 1:
        return 1
    ret = 1
    while n != 1:
        ret *= n
        n -= 1
    return ret


t = int(input())
for i in range(t):
    s = input()
    l = [0] * 10
    for i in s:
        l[int(i)] += 1
    c4 = l[4]
    c7 = l[7]
    p = factor(c4 + c7 - 2)
    r = reduce(lambda x, y: x * y, range(l[4] + l[7], len(s)), 1)
    dv = reduce(lambda x, y: x * factor(y), l, 1)
    ans = (factor(len(s)) - p * c4 * c7 * r) / dv
    print(ans % 1000000007)

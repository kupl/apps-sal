import math


def solve(s):
    li = s.split()
    n = len(li)
    l = len(li[0])
    m = ''
    for i in range(1, n):
        if l >= len(li[i]):
            l = len(li[i])
            m = li[i]
    res = ''
    res += m
    for i in li:
        res += ' '
        res += i
        res += ' '
        res += m
    print(res)


def __starting_point():
    try:
        s = input().strip()
        solve(s)
    except:
        pass


__starting_point()

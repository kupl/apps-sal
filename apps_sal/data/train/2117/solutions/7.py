import sys


def solve():
    (n,) = rv()
    (h,) = rl(1)
    smallertoleftindex = [-1] * n
    smallertorightindex = [n] * n
    temp = list()
    for i in range(n):
        while len(temp) > 0 and h[temp[-1]] >= h[i]:
            temp.pop(-1)
        smallertoleftindex[i] = -1 if len(temp) == 0 else temp[-1]
        temp.append(i)
    temp = list()
    for i in range(n - 1, -1, -1):
        while len(temp) > 0 and h[temp[-1]] >= h[i]:
            temp.pop(-1)
        smallertorightindex[i] = n if len(temp) == 0 else temp[-1]
        temp.append(i)
    res = [0] * (n + 1)
    for i in range(n):
        nums = smallertorightindex[i] - smallertoleftindex[i] - 1
        res[nums] = max(res[nums], h[i])
    for i in range(n - 1, 0, -1):
        res[i] = max(res[i], res[i + 1])
    print(' '.join(map(str, res[1:])))


def prt(l):
    return print(''.join(l))


def rv():
    return map(int, input().split())


def rl(n):
    return [list(map(int, input().split())) for _ in range(n)]


if sys.hexversion == 50594544:
    sys.stdin = open('test.txt')
solve()

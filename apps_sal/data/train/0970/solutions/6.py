import sys
from sys import stdin, stdout
from bisect import bisect_right
from os import path


def cinN(): return (int(stdin.readline()))
def cin(): return(map(int, stdin.readline().split()))


def find_le(a, x):
    'Find rightmost value less than or equal to x'
    i = bisect_right(a, x)
    if i:
        return i - 1
    return -1


def func():
    n = cinN()
    l = list(cin())
    l.sort()
    qn = cinN()
    for _ in range(qn):
        x, y = cin()
        k = x + y
        t = find_le(l, k)
        if t == -1:
            ans = (0)
        else:
            if l[t] == k:
                ans = (-1)
            else:
                ans = (t + 1)
        print(ans)


def __starting_point():
    test = cinN()
    for _ in range(test):
        func()


__starting_point()

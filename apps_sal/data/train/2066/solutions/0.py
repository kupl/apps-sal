import os
import random
import sys
from typing import List, Dict


class Int:
    def __init__(self, val):
        self.val = val

    def get(self):
        return self.val + 111


class Unique:
    def __init__(self):
        self.s = set()

    def add(self, val: int):
        self.s.add(val)

    def __contains__(self, item: int) -> bool:
        return self.s.__contains__(item)


def ceil(top: int, bottom: int) -> int:
    return (top + bottom - 1) // bottom


def concat(l: List[int]):
    return "".join(map(str, l))


def get(d: Dict[int, str], val: int) -> Dict[int, str]:
    return d[val]


def slowsolve(a):
    a.sort()
    small = True
    while len(a) > 2:
        if small:
            if a[1] - a[0] > a[-1] - a[-2]:
                a.pop(0)
            else:
                a.pop()
            small = False
        else:
            a.pop(len(a) // 2)
            small = True

    return a[1] - a[0]


def solve(a):
    a.sort()
    candelete = len(a) // 2 - 1
    res = 10 ** 18
    for leftdelete in range(0, candelete + 1):
        leftrem = leftdelete
        rightrem = leftdelete + candelete + 1
        res = min(res, a[rightrem] - a[leftrem])
    return res


def prt(l): return print(' '.join(l))
def rv(): return map(int, input().split())
def rl(n): return [list(map(int, input().split())) for _ in range(n)]


if os.path.exists("test.txt"):
    sys.stdin = open("test.txt")

n, = rv()
a, = rl(1)

print(solve(a))

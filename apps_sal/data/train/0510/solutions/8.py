# -*- coding: utf-8 -*-

'''
7
abcdbbd
6
2 3 6
1 5 z
2 1 1
1 4 a
1 7 d
2 1 7
'''

# from helper import elapsed_time
from bisect import bisect_left, insort_left


N = int(input())
s = list(input())
Q = int(input())

# a-zまでの26文字に対して、s文字列の各文字に該当するindexを格納しておく
d = {i: [] for i in range(26)}
for i, c in enumerate(s):
    d[ord(c) - ord("a")].append(i)


# @elapsed_time
def convert(d: dict, s: list, q1: int, q2: str):
    if s[q1] == q2:
        return d, s

    didx_before = ord(s[q1]) - ord("a")
    didx_after = ord(q2) - ord("a")

    idx = bisect_left(d[didx_before], q1)
    d[didx_before].pop(idx)
    s[q1] = q2
    insort_left(d[didx_after], q1)

    return d, s


# @elapsed_time
def calc(d: dict, q1: int, q2: int):
    ans = 0
    for i in range(26):
        idx = bisect_left(d[i], q1)
        if d[i] and q1 <= d[i][-1] and d[i][idx] < q2 + 1:
            ans += 1

    return ans


for _ in range(Q):
    q, q1, q2 = input().split()
    q = int(q)
    if q == 1:
        d, s = convert(d, s, int(q1) - 1, q2)
    if q == 2:
        print((calc(d, int(q1) - 1, int(q2) - 1)))


#!/usr/bin python3
# -*- coding: utf-8 -*-

from bisect import bisect_left, bisect_right


n = int(input())
s = list(input())
q = int(input())

al = 'abcdefghijklmnopqrstuvwxyz'
dicq = {i: [] for i in al}
for i, si in enumerate(s):
    dicq[si].append(i)


def q1(iq, cq):
    #print(iq,cq,s[iq],dicq[s[iq]],bisect_left(dicq[s[iq]], iq))
    dicq[s[iq]].pop(bisect_left(dicq[s[iq]], iq))  # 更新前から削除
    s[iq] = cq
    dicq[cq].insert(bisect_left(dicq[cq], iq), iq)  # 更新後に追加


def q2(l, r):
    ret = 0
    for ai in al:
        if len(dicq[ai]) == 0:
            continue
        li = bisect_left(dicq[ai], l)
        ri = bisect_right(dicq[ai], r)
        if li != ri:
            ret += 1
        elif li == len(dicq[ai]):
            continue
        elif dicq[ai][li] == l:
            ret += 1
    #    print(l,r,ai,dicq[ai],li,ri,ret)
    print(ret)


for i in range(q):
    fg, x, y = input().split()
    if fg == '1':
        q1(int(x) - 1, y)
    else:
        q2(int(x) - 1, int(y) - 1)

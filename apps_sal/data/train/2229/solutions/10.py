import heapq
from bisect import bisect_left, bisect_right
from itertools import accumulate


def is_substr(fw, tw, seq):
    (i, j) = (0, 0)
    while i < len(fw) and j < len(tw):
        if i in seq:
            i += 1
        elif fw[i] == tw[j]:
            (i, j) = (i + 1, j + 1)
        else:
            i += 1
    return j == len(tw)


def R():
    return map(int, input().split())


(fw, tw) = (input(), input())
seq = [i - 1 for i in list(R())]
(l, r) = (0, len(seq) - 1)
(m, res) = (0, 0)
while l <= r:
    m = (l + r) // 2
    if is_substr(fw, tw, set(seq[:m])):
        res = max(res, m)
        l = m + 1
    else:
        r = m - 1
print(res)

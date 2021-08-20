from string import ascii_lowercase
import bisect
import sys


def input():
    return sys.stdin.readline().rstrip()


sys.setrecursionlimit(10 ** 7)
d = dict()
for (i, c) in enumerate(ascii_lowercase):
    d[c] = i
N = int(input())
S = list(input())
lst = [[] for _ in range(26)]
for i in range(N):
    lst[d[S[i]]].append(i)
Q = int(input())
for q in range(Q):
    (a, b, c) = input().split()
    if a == '1':
        i = int(b) - 1
        if c == S[i]:
            continue
        idx = bisect.bisect_left(lst[d[S[i]]], i)
        del lst[d[S[i]]][idx]
        bisect.insort_left(lst[d[c]], i)
        S[i] = c
    else:
        l = int(b) - 1
        r = int(c)
        ans = 0
        for i in range(26):
            cnt = bisect.bisect_left(lst[i], r) - bisect.bisect_left(lst[i], l)
            if cnt:
                ans += 1
        print(ans)

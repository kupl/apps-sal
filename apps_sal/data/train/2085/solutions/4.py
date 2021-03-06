import math
import collections
import bisect
import heapq
import time
import random
'\ncreated by shhuan at 2017/10/5 15:00\n\n'
N = int(input())
S = ['']
for i in range(N):
    S.append(input())
M = int(input())
A = [[set() for _ in range(10)] for _ in range(M + N + 1)]
D = collections.defaultdict(int)
for i in range(1, N + 1):
    for j in range(1, 10):
        s = S[i]
        if j > len(s):
            break
        for k in range(len(s) - j + 1):
            A[i][j].add(int(s[k:k + j], 2))
        if all((v in A[i][j] for v in range(2 ** j))):
            D[i] = j
for i in range(M):
    (a, b) = list(map(int, input().split()))
    (s, sa, sb) = (S[a] + S[b], S[a], S[b])
    if len(s) > 30:
        S.append(s[:10] + s[-10:])
    else:
        S.append(s)
    ai = i + N + 1
    d = max(D[a], D[b]) + 1
    for dv in range(d, 10):
        if len(sa) + len(sb) < dv:
            break
        A[ai][dv] = A[a][dv] | A[b][dv] | {int(v, 2) for v in {sa[-i:] + sb[:dv - i] for i in range(1, dv + 1)} if len(v) == dv}
    ans = d - 1
    for dv in range(d, 10):
        if any((v not in A[ai][dv] for v in range(2 ** dv))):
            break
        ans = dv
    print(ans)
    D[ai] = ans

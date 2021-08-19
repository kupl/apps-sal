from bisect import bisect_left
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
dics = []
q = []
Ind = []
ans = [0] * N
for (i, a) in enumerate(A):
    ia = bisect_left(q, a)
    if ia == len(q):
        Ind.append(i)
        q.append(a)
        dics.append({a: 1})
    else:
        dic = dics[ia]
        if not a in dic.keys():
            dic[a] = 1
        else:
            dic[a] += 1
L = len(q)
for l in reversed(range(L)):
    if l == 0:
        for (k, v) in dics[0].items():
            ans[Ind[0]] += k * v
    else:
        bef = q[l - 1]
        for (k, v) in dics[l].items():
            ans[Ind[l]] += (k - bef) * v
            dics[l - 1][bef] += v
for a in ans:
    print(a)

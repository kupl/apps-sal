from bisect import bisect_left
import sys
sys.setrecursionlimit(10**8)
N = int(input())
A = list(map(int, input().split()))
UV = [tuple(map(int, input().split())) for i in range(N - 1)]
es = [[] for _ in range(N)]
for u, v in UV:
    u, v = u - 1, v - 1
    es[u].append(v)
    es[v].append(u)

lis = [A[0]]
stack = []
ans = [1] * N


def dfs(v, p=-1):
    for to in es[v]:
        if to == p:
            continue
        i = bisect_left(lis, A[to])
        if i == len(lis):
            stack.append((i, -1))
            lis.append(A[to])
        else:
            stack.append((i, lis[i]))
            lis[i] = A[to]
        ans[to] = len(lis)

        dfs(to, v)

        i, a = stack.pop()
        if a < 0:
            lis.pop()
        else:
            lis[i] = a


dfs(0)
print(*ans, sep='\n')

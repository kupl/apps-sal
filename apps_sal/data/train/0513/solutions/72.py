import collections
import bisect
import sys

sys.setrecursionlimit(10 ** 8)


def f(v):
    state[v] = 1
    a = As[v]
    idx = bisect.bisect_left(D, a)
    stack.append((idx, D[idx]))  # push
    D[idx] = a

    ans[v] = bisect.bisect_left(D, float('inf'))

    for u in V[v]:
        if state[u] == 0:
            f(u)

    # 巻き戻し
    i_pre, d_pre = stack.pop()
    D[i_pre] = d_pre


N = int(input())
As = list(map(int, input().split()))

D = [float('inf')] * N
stack = collections.deque([])
ans = [0] * N
state = [0] * N

V = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    V[u - 1].append(v - 1)
    V[v - 1].append(u - 1)

f(0)

print(*ans, sep='\n')

from bisect import bisect_left
n = int(input())
A = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    (u, v) = map(int, input().split())
    graph[v].append(u)
    graph[u].append(v)
start = 1
stack = [1]
par = [-1] * (n + 1)
ans = [0] * (n + 1)
used = [False] * (n + 1)
infi = 10 ** 20
LIS = [infi] * (n + 1)
LIS[0] = -infi
position = [(-1, -1)] * (n + 1)


def hantei(val, L):
    pos = bisect_left(L, val)
    pre = L[pos]
    L[pos] = val
    cnt = bisect_left(L, infi)
    return (L, pos, pre, cnt)


while stack:
    v = stack[-1]
    if not used[v]:
        (LIS, pos, pre, cnt) = hantei(A[v], LIS)
        position[v] = (pos, pre)
        ans[v] = cnt - 1
    used[v] = True
    if not graph[v]:
        _ = stack.pop()
        (basho, atai) = position[v]
        LIS[basho] = atai
        continue
    u = graph[v].pop()
    if u == par[v]:
        continue
    par[u] = v
    stack.append(u)
print(*ans[1:], sep='\n')

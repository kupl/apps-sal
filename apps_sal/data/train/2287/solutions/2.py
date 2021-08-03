import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())
G = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)
K = int(input())
num = [-1] * (N + 1)
for _ in range(K):
    V, P = map(int, input().split())
    num[V] = P

# check parity
stack = [1]
depth = [-1] * (N + 1)
depth[1] = 0
while stack:
    v = stack.pop()
    for c in G[v]:
        if depth[c] == -1:
            depth[c] = depth[v] + 1
            stack.append(c)
parity = [set(), set()]
for i in range(1, N + 1):
    if num[i] != -1:
        parity[depth[i] % 2].add(num[i] % 2)
if len(parity[0]) == 2 or len(parity[1]) == 2:
    print('No')
    return

INF = 10**9
lb = [-INF] * (N + 1)
ub = [INF] * (N + 1)


def dfs1(v, p):
    for c in G[v]:
        if c == p:
            continue
        dfs1(c, v)
        lb[v] = max(lb[v], lb[c] - 1)
        ub[v] = min(ub[v], ub[c] + 1)
    if num[v] != -1:
        lb[v] = ub[v] = num[v]


dfs1(1, 0)


def dfs2(v, p):
    for c in G[v]:
        if c == p:
            continue
    for c in G[v]:
        if c == p:
            continue
        lb[c] = max(lb[c], lb[v] - 1)
        ub[c] = min(ub[c], ub[v] + 1)
        dfs2(c, v)


dfs2(1, 0)

for i in range(1, N + 1):
    if lb[i] > ub[i]:
        print('No')
        return

print('Yes')


def dfs3(v, p):
    for c in G[v]:
        if c == p:
            continue
        if lb[c] <= num[v] - 1:
            num[c] = num[v] - 1
        else:
            num[c] = num[v] + 1
        dfs3(c, v)


num[1] = lb[1]
dfs3(1, 0)

print(*num[1:], sep='\n')

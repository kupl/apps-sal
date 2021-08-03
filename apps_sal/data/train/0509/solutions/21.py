import sys

input = sys.stdin.readline
N, M = map(int, input().split())
uvc = [list(map(int, input().split())) for _ in range(M)]

edge = [[] for i in range(N)]
for u, v, c in uvc:
    u -= 1
    v -= 1
    c -= 1
    edge[u].append((v, c))
    edge[v].append((u, c))

label = [-1] * N
label[0] = 0

Q = [0]
while Q:
    v = Q.pop()
    for u, l in edge[v]:
        if label[u] != -1:
            continue
        Q.append(u)
        if label[v] != l:
            label[u] = l
        else:
            label[u] = l + 1

print(*(l + 1 for l in label), sep="\n")

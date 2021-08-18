from collections import deque

N, M = list(map(int, input().split()))
uvc = [list(map(int, input().split())) for _ in range(M)]

G = [[] for _ in range(N + 1)]
for i in range(M):
    A = uvc[i][0]
    B = uvc[i][1]
    G[A].append([B, uvc[i][2]])
    G[B].append([A, uvc[i][2]])

seen = [0] * (N + 1)
seen[1] = G[1][0][1]
q = deque([1])
while q:
    t = q.pop()
    for p, e in G[t]:
        if seen[p] > 0:
            continue
        if seen[t] != e:
            seen[p] = e
        else:
            if seen[t] + 1 <= N:
                seen[p] = seen[t] + 1
            elif seen[t] - 1 > 0:
                seen[p] = seen[t] - 1
        q.append(p)

for i in range(1, N + 1):
    if seen[i] == 0:
        print('No')
        return

for i in range(1, N + 1):
    print((seen[i]))

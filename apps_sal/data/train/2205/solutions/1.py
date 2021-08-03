import sys
from collections import deque
readline = sys.stdin.readline

H, W, T = map(int, readline().split())
G = [-1] * (W + 2)
for _ in range(H):
    G.extend([-1] + list(map(int, readline().strip())) + [-1])
G.extend([-1] * (W + 2))

geta = W + 2
of1 = set()
DIREC = [1, -1, W + 2, -W - 2]
Q = []

for vn in range((H + 2) * (W + 2)):
    if G[vn] == -1:
        continue
    for dv in DIREC:
        if G[vn] == G[vn + dv]:
            Q.append(vn)
            break


if not Q:
    for qu in range(T):
        i, j, p = map(int, readline().split())
        vn = i * geta + j
        sys.stdout.write(str(G[vn]) + '\n')
else:
    dist = [0] * ((H + 2) * (W + 2))
    used = set(Q)
    Q = deque(Q)
    while Q:
        vn = Q.pop()
        for dv in DIREC:
            if G[vn + dv] == -1 or vn + dv in used:
                continue
            used.add(vn + dv)
            dist[vn + dv] = 1 + dist[vn]
            Q.appendleft(vn + dv)
    for qu in range(T):
        i, j, p = map(int, readline().split())
        vn = i * geta + j
        if dist[vn] >= p:
            ans = G[vn]
        else:
            ans = G[vn] ^ (1 & (p - dist[vn]))
        sys.stdout.write(str(ans) + '\n')

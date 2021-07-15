#!/usr/bin python3
# -*- coding: utf-8 -*-

# https://atcoder.jp/contests/arc061/tasks/arc061_c

########################################################
# 01BFS
########################################################

from collections import deque

n, m = list(map(int, input().split()))
ab = set([])
ps = set([i<<20 for i in range(1, n+1)])

for _ in range(m):
    a, b, c = list(map(int, input().split()))
    a <<= 20
    b <<= 20
    ps.add(a+c)
    ps.add(b+c)
    ab.add((a, b, c))


psr = {ps:i for i, ps in enumerate(ps)}
psc = len(ps)
gmap = [[] for _ in range(psc)]
for a, b, c in ab:
    a0 = psr[a]
    b0 = psr[b]
    a1 = psr[a+c]
    b1 = psr[b+c]
    gmap[a0].append((a1, 1))
    gmap[b0].append((b1, 1))
    gmap[a1].append((a0, 0))
    gmap[b1].append((b0, 0))
    gmap[a1].append((b1, 0))
    gmap[b1].append((a1, 0))

INF = float('inf')
dist = [INF] * psc

def zero_one_bfs(sp, gp):
    next_q = deque([])
    next_q.append(sp)
    dist[sp] = 0
    while next_q:
        cp = next_q.popleft()
        cd = dist[cp]
        if cp == gp: return cd
        for np, pay in gmap[cp]:
            if dist[np] <= cd+pay: continue
            dist[np] = cd + pay
            if pay == 1:
                next_q.append(np)
            else:
                next_q.appendleft(np)
    return dist[gp]

ret = zero_one_bfs(psr[1<<20], psr[n<<20])
print((-1 if ret == INF else ret))


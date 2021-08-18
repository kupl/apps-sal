from collections import deque
import sys
readline = sys.stdin.readline
read = sys.stdin.read

n, m = list(map(int, readline().split()))

g = {}

for _ in range(m):
    p, q, c = list(map(int, readline().split()))
    pc = ((p - 1) << 20) + c
    qc = ((q - 1) << 20) + c
    pp = (p - 1) << 20
    qq = (q - 1) << 20

    if pc not in g:
        g[pc] = []
    if qc not in g:
        g[qc] = []
    if pp not in g:
        g[pp] = []
    if qq not in g:
        g[qq] = []

    g[pc].append(qc)
    g[pc].append(pp)

    g[qc].append(pc)
    g[qc].append(qq)

    g[pp].append(pc)
    g[qq].append(qc)

if 0 not in g:
    g[0] = []

q = deque([(0, 0)])
res = {0: 0}

mask = (1 << 20) - 1
while q:
    vl, dv = q.popleft()
    if res[vl] < dv:
        continue
    if (vl >> 20) == n - 1:
        res[(n - 1) << 20] = dv + 1
        break
    for tl in g[vl]:
        ndv = dv + (vl & mask == 0 or tl & mask == 0)
        if tl not in res or res[tl] > ndv:
            res[tl] = ndv
            if vl & mask == 0 or tl & mask == 0:
                q.append((tl, ndv))
            else:
                q.appendleft((tl, ndv))

if (n - 1) << 20 in res:
    print((res[(n - 1) << 20] // 2))
else:
    print((-1))

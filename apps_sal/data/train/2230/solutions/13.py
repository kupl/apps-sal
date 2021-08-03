import sys
from collections import deque
def read(): return sys.stdin.readline().rstrip()
def readi(): return int(sys.stdin.readline())
def writeln(x): return sys.stdout.write(str(x) + "\n")
def write(x): return sys.stdout.write(x)


N = readi()
ps = list(map(int, read().split()))
cas = list(map(int, read().split()))
cbs = list(map(int, read().split()))
M = readi()
bs = list(map(int, read().split()))
results = []
ts = [[] for _ in range(7)]
tcnt = [0 for _ in range(7)]
for i in range(N):
    price, a, b = ps[i], cas[i], cbs[i]
    color = 2**(a - 1) | 2**(b - 1)
    ts[color].append(price)
    tcnt[color] += 1

tss = []
for i in range(7):
    if tcnt[i]:
        tss.append(deque(list(sorted(ts[i]))))
    else:
        tss.append([])

spots = [[1, 3, 5], [3, 2, 6], [5, 6, 4]]
for i in range(M):
    s1, s2, s3 = spots[bs[i] - 1]

    c1, c2, c3 = tcnt[s1], tcnt[s2], tcnt[s3]
    alts = []
    if c1:
        alts.append(s1)
    if c2:
        alts.append(s2)
    if c3:
        alts.append(s3)
    if not alts:
        results.append("-1")
        continue

    vals = []
    for alt in alts:
        vals.append((tss[alt][0], alt))
    vals.sort()
    price, cidx = vals[0]
    results.append(str(price))
    tcnt[cidx] -= 1
    tss[cidx].popleft()
writeln(" ".join(results))

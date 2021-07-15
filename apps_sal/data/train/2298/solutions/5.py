import sys

N, T = list(map(int, sys.stdin.readline().rstrip().split()))

As = []
As = list(map(int, sys.stdin.readline().rstrip().split()))

mins = []
m = 1e10
vs = []
for A in As:
    m = min(m, A)
    vs.append(A - m)
max_v = max(vs)
res = 0
for v in vs:
    if v == max_v:
        res += 1
print(res)



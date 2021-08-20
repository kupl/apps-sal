import sys
read = sys.stdin.read
readline = sys.stdin.readline
(x,) = map(int, readline().split())
(k,) = map(int, readline().split())
(*r,) = map(int, readline().split())
(q,) = map(int, readline().split())
r.append(1 << 30)
INF = 1 << 30
ID_M = (-INF, INF, 0)


def compose(lst1, lst2):
    return (funcval(lst1[0], lst2), funcval(lst1[1], lst2), lst1[2] + lst2[2])


def funcval(x, lst):
    (a, b, c) = lst
    if x <= a - c:
        return a
    elif x >= b - c:
        return b
    else:
        return x + c


seg = (0, x, 0)
tai = []
for i in range(q):
    (t, a) = map(int, readline().split())
    tai.append((t, a, i))
tai.sort(key=lambda x: x[0])
idx = 0
ans = [0] * q
t0 = 0
coeff = -1
for (i, ri) in enumerate(r):
    while idx < q and tai[idx][0] < ri:
        (t, a, j) = tai[idx]
        v = funcval(a, seg)
        ans[j] = min(x, max(v + coeff * (t - t0), 0))
        idx += 1
    seg = compose(seg, (0, x, coeff * (ri - t0)))
    t0 = ri
    coeff *= -1
print(*ans, sep='\n')

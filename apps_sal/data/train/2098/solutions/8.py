import sys


def pro():
    return sys.stdin.readline().strip()


def rop():
    return map(int, pro().split())


a, s = rop()
q = [0] * a
w = [0] * s
for i in range(a):
    n, p = rop()
    q[i] = (p, n - 1)
    w[n - 1] += 1
q.sort()
t = 1e100
for k in range(1, a + 1):
    p = w[::]
    r = [True] * a
    m = 0
    for i in range(a):
        po, rty = q[i]
        if rty != 0 and p[rty] >= k:
            p[0] += 1
            p[rty] -= 1
            m += po
            r[i] = False
    for i in range(a):
        po, rty = q[i]
        if rty != 0 and r[i] and p[0] < k:
            p[0] += 1
            p[rty] -= 1
            m += po
            r[i] = False
    t = min(t, m)
print(t)

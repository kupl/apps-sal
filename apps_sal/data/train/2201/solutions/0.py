import sys
n = int(sys.stdin.readline())
a = [int(x) for x in sys.stdin.readline().split()]

eps = 1e-12

def f(x):
    mx = a[0] - x
    tsmx = 0.0
    mn = a[0] - x
    tsmn = 0.0
    for ai in a:
        tsmx = max(tsmx + ai - x, ai - x)
        mx = max(tsmx, mx)
        tsmn = min(tsmn + ai - x, ai - x)
        mn = min(tsmn, mn)

    return abs(mx), abs(mn)

l = min(a)
r = max(a)
f1, f2 = f(l)
for i in range(0, 90):
    m = (l + r) / 2
    f1, f2 = f(m)
    if f1 > f2:
        l = m
    else:
        r = m

A, B = f(l)
print(min(A,B))

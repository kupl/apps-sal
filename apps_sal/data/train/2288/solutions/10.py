import sys
input = sys.stdin.readline
x = int(input())
k = int(input())
R = [(_r, i % 2) for (i, _r) in enumerate(map(int, input().split()))]
n = int(input())
TA = [list(map(int, input().split())) for _ in range(n)]
(T, A) = zip(*TA)
L = [None] * n
b = 0
for (i, t) in enumerate(T, 1):
    R.append((t, -i))
R.sort()
dx = 1
(l, r, p, q) = (0, x, 0, x)
for (_r, i) in R:
    d = _r - b
    b = _r
    if dx == 1:
        if d <= p:
            p -= d
            q -= d
        elif d < q:
            q -= d
            l = r - q
            p = 0
        else:
            l = 0
            r = 0
            p = 0
            q = 0
    elif d <= x - q:
        p += d
        q += d
    elif d < x - p:
        p += d
        r = l + (x - p)
        q = x
    else:
        l = x
        r = x
        p = x
        q = x
    if i >= 0:
        dx = i
    else:
        a = A[-i - 1]
        if a < l:
            res = p
        elif a <= r:
            res = a - l + p
        else:
            res = q
        L[-i - 1] = res
print(*L, sep='\n')

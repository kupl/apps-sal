x = int(input())
k = int(input())
(*R,) = map(int, input().split() + [1 << 30])
Q = int(input())
ta = [tuple(map(int, input().split())) for _ in range(Q)]


def f(x, l):
    return max(l[0], min(l[1], x + l[2]))


L = (a, b, c) = (0, x, 0)
idx = t0 = 0
g = -1
for r in R:
    while idx < Q and ta[idx][0] < r:
        print(f(f(ta[idx][1], L) + g * (ta[idx][0] - t0), (0, x, 0)))
        idx += 1
    (d, t0) = (g * (r - t0), r)
    L = (a, b, c) = (f(a, (0, x, d)), f(b, (0, x, d)), c + d)
    g *= -1

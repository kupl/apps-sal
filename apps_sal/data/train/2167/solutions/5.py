def f():
    return list(map(int, input().split()))


(n, m) = f()
t = list(f())
p = [1000000000.0] + [abs(b - a) for (a, b) in zip(t, t[1:])] + [1000000000.0]
(L, R) = ([0] * n, [0] * n)
for i in range(1, n):
    j = n - i
    (x, y) = (i - 1, j + 1)
    (a, b) = (p[i], p[j])
    while a > p[x]:
        x = L[x]
    while b >= p[y]:
        y = R[y]
    (L[i], R[j]) = (x, y)
for k in range(m):
    (l, r) = f()
    print(sum(((i - max(l - 1, L[i])) * (min(r, R[i]) - i) * p[i] for i in range(l, r))))

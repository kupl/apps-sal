def f(x, y, z): return max(x, y, z) - min(x, y, z) > 1


t = input()
n, m, p = len(t), int(input()), {'x': 0, 'y': 1, 'z': 2}
s = [[0] * (n + 1) for i in range(3)]
for i, c in enumerate(t, 1):
    s[p[c]][i] = 1
for i in range(3):
    r = s[i]
    for j in range(1, n):
        r[j + 1] += r[j]
a, b, c = s
q, d = [map(int, input().split()) for i in range(m)], ['YES'] * m
for i, (l, r) in enumerate(q):
    if r - l > 1 and f(a[r] - a[l - 1], b[r] - b[l - 1], c[r] - c[l - 1]):
        d[i] = 'NO'
print('\n'.join(d))

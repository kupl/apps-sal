def f(t): return t[2] - t[0] > 1
t = input()
n, m, p = len(t), int(input()), {'x': 0, 'y': 1, 'z': 2}
s = [[0] * (n + 1) for i in range(3)]
for i, c in enumerate(t, 1): s[p[c]][i] = 1
for i in range(3):
    for j in range(1, n): s[i][j + 1] += s[i][j]
a, b, c = s
q, d = [map(int, input().split()) for i in range(m)], ['YES'] * m
for i, (l, r) in enumerate(q):
    if r - l > 1 and f(sorted([a[r] - a[l - 1], b[r] - b[l - 1], c[r] - c[l - 1]])): d[i] = 'NO'
print('\n'.join(d))

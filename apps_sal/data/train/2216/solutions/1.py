def f(x, y, z): return abs(y - x) > 1 or abs(z - x) > 1 or abs(y - z) > 1
t = input()
n, p = len(t), {'x': 0, 'y': 1, 'z': 2}
s = [[0] * (n + 1) for i in range(3)]
for i, c in enumerate(t, 1): s[p[c]][i] = 1
for i in range(3):
    for j in range(1, n): s[i][j + 1] += s[i][j]
a, b, c = s
q = [map(int, input().split()) for i in range(int(input()))]
d = ['YES'] * len(q)
for i, (l, r) in enumerate(q):
    if r - l > 1 and f(a[r] - a[l - 1], b[r] - b[l - 1], c[r] - c[l - 1]): d[i] = 'NO'
print('\n'.join(d))

(n, m) = (337, int(input()))
p = [['N'] * n for i in range(n)]


def f(i, j):
    p[i][j] = p[j][i] = 'Y'


k = 6 + 15 * 5
for j in range(2, 6):
    f(1, j)
for i in range(6, k, 5):
    for j in range(i - 4, i):
        f(i, j)
    for j in range(i + 1, i + 5):
        f(i, j)
(q, d, s) = (4 ** 15, 0, k)
while q:
    if m >= q:
        t = m // q
        m -= t * q
        if d == 0:
            for j in range(k - t, k):
                f(0, j)
        else:
            f(0, s)
            for i in range(s, s + d):
                f(i, i + 1)
            s += d
            for j in range(k - t, k):
                f(s, j)
            s += 1
    k -= 5
    d += 2
    q //= 4
print(s)
for i in range(s):
    print(''.join(p[i][:s]))

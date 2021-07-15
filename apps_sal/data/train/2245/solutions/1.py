n, m, k = map(int, input().split())
t = list(map(int, input().split()))
p = [tuple(map(int, input().split())) for i in range(m)]

r, s = [0] * (m + 1), [0] * (n + 1)
R, S = 0, 0

for i in range(k):
    x, y = map(int, input().split())
    r[x - 1] += 1
    r[y] -= 1

for i, (x, y, d) in enumerate(p):
    R += r[i]
    d = d * R
    s[x - 1] += d
    s[y] -= d

for i in range(n):
    S += s[i]
    t[i] = str(t[i] + S)

print(' '.join(map(str, t)))

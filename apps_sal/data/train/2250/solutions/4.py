def f(): return map(int, input().split())


n, m, k = f()

w, h = 2 * n, 2 * m
s = [[] for i in range(w + h)]
p = [-1] * k

for i in range(k):
    x, y = f()
    if x - y & 1:
        continue

    for a in (x, w - x):
        for b in (y, h - y):
            s[b - a].append((a, i))

a = b = t = 0
while 1:
    for x, i in s[b - a]:
        if p[i] < 0:
            p[i] = t + x - a

    d = min(w - a, h - b)
    t += d

    a = (a + d) % w
    b = (b + d) % h

    if a % n == b % m:
        break

for q in p:
    print(q)

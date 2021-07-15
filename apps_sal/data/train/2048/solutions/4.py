from sys import *
f = lambda: map(int, stdin.readline().split())
n, k = f()
t = sorted(f())
s = [0] * (n + 1)
for i in range(n): s[i + 1] = s[i] + t[i]
t = [0] + t
d = s[n]
l, r = 0, n
while l < r:
    m = l + r + 1 >> 1
    if t[m] * m - s[m] > k: r = m - 1
    else: l = m
x = l
l, r = 0, n
while l < r:
    m = l + r >> 1
    if d - s[m] - t[m] * (n - m) > k: l = m + 1
    else: r = m
y = r
q = (d - s[y - 1] - k + n - y) // (n - y + 1) - (s[x] + k) // x
print(max(q, int(d % n > 0)))

def f():
    return list(map(int, input().split()))


(n, k) = f()
p = sorted(f())
(m, d) = (n // k, n % k)
(u, v) = (d + 1, k - d + 1)
g = [0] * u * v
i = 0
for a in range(u):
    j = a * m + a - 1
    for b in range(v):
        x = g[i - 1] + p[j] - p[j - m + 1] if b else 9000000000.0
        y = g[i - v] + p[j] - p[j - m] if a else 9000000000.0
        if i:
            g[i] = min(x, y)
        i += 1
        j += m
print(g[-1])

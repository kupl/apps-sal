n, m = int(input()), 150001
p = [m] + list(map(int, input().split())) + [m * (n & 1)]
f = lambda i: p[i] >= p[i + 1] if i & 1 else p[i] <= p[i + 1]
g = lambda i, j: sum(f(k) for k in {i, i - 1, j, j - 1})
t = [f(i) for i in range(n + 1)]
r, s = 0, sum(t)
if s > 4: print(0);return
e = {i + 1 for i in range(n) if t[i] or t[i + 1]}
for i in e:
    for j in range(1, n + 1):
        if (i < j or (i > j and j not in e)) and g(i, j) == s:
            p[i], p[j] = p[j], p[i]
            r += g(i, j) == 0
            p[i], p[j] = p[j], p[i]
print(r)

def inf():
    return map(int, input().split())


(n,) = inf()
a = list(inf())
p = sorted([i for i in range(n)], key=lambda x: a[x])
b = [0] * n
for i in range(n):
    b[p[i]] = a[p[(i + 1) % n]]
for i in range(n):
    print(b[i], end=' ')
print()

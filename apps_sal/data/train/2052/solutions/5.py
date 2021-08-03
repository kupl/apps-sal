n, m = map(int, input().split())
k = n + 1
a, b = [0] * k, [0] * k
a[0] = a[1] = a[n] = b[0] = b[1] = b[n] = 1
for i in range(m):
    x, y = map(int, input().split())
    a[x] = b[y] = 1
s = a.count(0) + b.count(0)
if n & 1 and 0 == a[k // 2] == b[k // 2]:
    s -= 1
print(s)

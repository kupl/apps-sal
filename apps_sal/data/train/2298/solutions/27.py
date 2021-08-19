(n, t) = map(int, input().split())
a = [int(i) for i in input().split()]
b = [0 for i in range(n)]
m = a[0]
for i in range(n):
    m = min(m, a[i])
    b[i] = a[i] - m
m = b[0]
k = 0
for i in range(n):
    if b[i] >= m:
        m = b[i]
        k = i
ans1 = 1
for i in range(n):
    if b[i] == m and i != k:
        ans1 += 1
b = [0 for i in range(n)]
m = a[n - 1]
for i in range(n - 1, -1, -1):
    m = max(m, a[i])
    b[i] = a[i] - m
m = b[n - 1]
k = 0
for i in range(n - 1, -1, -1):
    if b[i] <= m:
        m = b[i]
        k = i
ans2 = 1
for i in range(n):
    if b[i] == m and i != k:
        ans2 += 1
print(min(ans1, ans2))

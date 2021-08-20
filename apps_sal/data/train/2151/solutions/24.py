(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
s = abs(m - a[n // 2])
for i in range(n // 2):
    if a[i] > m:
        s += a[i] - m
for i in range(n // 2 + 1, n):
    if a[i] < m:
        s += m - a[i]
print(s)

(n, s) = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
ans = abs(a[n // 2] - s)
a[n // 2] = s
for i in range(n // 2, n - 1):
    if a[i] > a[i + 1]:
        ans += a[i] - a[i + 1]
        a[i + 1] = a[i]
for i in range(n // 2, 0, -1):
    if a[i] < a[i - 1]:
        ans += a[i - 1] - a[i]
        a[i - 1] = a[i]
print(ans)

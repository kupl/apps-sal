(n, s) = list(map(int, input().split()))
a = sorted(list(map(int, input().split())))
ans = abs(a[n // 2] - s)
for i in range(n // 2):
    if a[i] > s:
        ans += a[i] - s
for i in range(n // 2 + 1, n):
    if a[i] < s:
        ans += s - a[i]
print(ans)

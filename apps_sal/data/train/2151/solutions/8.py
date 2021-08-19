(n, s) = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
a = sorted(a)
m = n // 2
ans = 0
if a[m] > s:
    while m >= 0 and a[m] > s:
        ans += a[m] - s
        m = m - 1
else:
    while m < n and a[m] < s:
        ans += s - a[m]
        m += 1
print(ans)

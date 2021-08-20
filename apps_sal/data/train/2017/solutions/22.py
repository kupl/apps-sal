n = int(input())
a = input().split()
for i in range(0, n + n):
    a[i] = int(a[i])
ans = 0
for i in range(0, 2 * n - 1, 2):
    x = a[i]
    if a[i] == a[i + 1]:
        continue
    idx = a.index(a[i], i + 1)
    ans += idx - i - 1
    del a[idx]
    a.insert(i + 1, a[i])
print(ans)

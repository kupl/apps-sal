(n, m) = map(int, input().split())
a = [[] for i in range(5010)]
for i in range(m):
    (x, y) = map(int, input().split())
    if y < x:
        a[x].append(n - x + y)
    else:
        a[x].append(y - x)
for i in range(1, n + 1):
    a[i].sort()
mx = int(-1000000000.0)
for i in range(1, n + 1):
    if len(a[i]):
        mx = n * (len(a[i]) - 1) + a[i][0]
    else:
        mx = 0
    k = 1
    l = i + 1
    if l == n + 1:
        l = 1
    while l != i:
        if len(a[l]):
            mx = max(mx, n * (len(a[l]) - 1) + a[l][0] + k)
        k += 1
        l += 1
        if l == n + 1:
            l = 1
    print(mx, end=' ')
print()

n = int(input())
a = [int(x) for x in input().split()]
a.sort()
if n * a[n - 1] - sum(a) >= a[n - 1]:
    print(a[n - 1])
else:
    p = 0
    for i in range(n - 2):
        p += a[n - 1] - a[n - i - 2]
    q = p
    q += a[n - 1] - a[0] + (a[0] - p) // (n - 1) * n + (a[0] - p) % (n - 1)
    if (a[0] - p) % (n - 1):
        q += 1
    print(q)

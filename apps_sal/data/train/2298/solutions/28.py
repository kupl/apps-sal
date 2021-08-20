(n, t) = map(int, input().split())
a = [int(x) for x in input().split()]
mx = [0] * n
mx[-1] = a[-1]
for i in range(n - 2, -1, -1):
    mx[i] = max(mx[i + 1], a[i])
d = 0
c = 0
for i in range(n - 1):
    cur = a[i]
    can = mx[i + 1]
    dd = can - cur
    if dd > d:
        d = dd
        c = 1
    elif dd == d:
        c += 1
print(c)

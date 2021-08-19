def R():
    return list(map(int, input().split()))


(n, m) = R()
a = R()
b = R()
a.sort()
b.sort()
M = a[n - 1]
test = 0
s = 0
for j in range(m):
    if b[j] < M:
        test = 1
        break
if test == 1:
    print(-1)
else:
    k = 0
    for i in range(m):
        if b[i] == a[n - 1]:
            k = 1
    if k == 1:
        s = sum(b) + (sum(a) - a[n - 1]) * m
        print(s)
    else:
        s = sum(b) + (sum(a) - a[n - 1] - a[n - 2]) * m + a[n - 2] * (m - 1) + a[n - 1]
        print(s)

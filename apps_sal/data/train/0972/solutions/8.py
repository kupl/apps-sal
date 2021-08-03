n, k = list(map(int, input().split()))
l = []
l2 = []
for i in range(n):
    a = int(input())
    l.append(a)
l.sort()
for i in range(n - k + 1):
    l1 = []
    for j in range(i, k + i):
        l1.append(l[j])
    hmax = max(l1)
    hmin = min(l1)
    d = hmax - hmin
    l2.append(d)
print(min(l2))

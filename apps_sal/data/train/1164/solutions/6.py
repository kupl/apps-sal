(p, s) = map(int, input().split())
l = []
for i in range(p):
    ns = list(map(int, input().split()))
    n = list(map(int, input().split()))
    a = list(zip(ns, n))
    a.sort()
    count = 0
    for j in range(len(a) - 1):
        if a[j][1] > a[j + 1][1]:
            count += 1
    l.append((i, count))
l.sort(key=lambda x: x[1])
for i in range(p):
    print(l[i][0] + 1)

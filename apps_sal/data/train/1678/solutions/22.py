(n, m) = map(int, input().split())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
a = [(l1[i], i) for i in range(n)]
b = [(l2[i], i) for i in range(m)]
a.sort(key=lambda x: x[0])
b.sort(key=lambda x: x[0])
for i in range(m):
    print(a[0][1], b[i][1])
for i in range(1, n):
    print(a[i][1], b[m - 1][1])

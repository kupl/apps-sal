(n, m) = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
al = [(a[i], i) for i in range(n)]
bl = [(b[i], i) for i in range(m)]
al.sort(key=lambda x: x[0])
bl.sort(key=lambda x: x[0])
for i in range(m):
    print(al[0][1], bl[i][1])
for i in range(1, n):
    print(al[i][1], bl[m - 1][1])

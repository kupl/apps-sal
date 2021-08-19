n = int(input())
a = list(map(int, input().split()))
q = int(int(input()))
for i in range(q):
    (x, y) = map(int, input().split())
    if x - 2 >= 0:
        a[x - 2] += y - 1
    if x < n:
        a[x] += a[x - 1] - y
    a[x - 1] = 0
for i in range(n):
    print(a[i])

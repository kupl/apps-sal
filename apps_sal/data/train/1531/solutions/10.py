n = int(input())
a = list(map(int, input().strip().split()))
m = int(input())
for i in range(m):
    (x, y) = map(int, input().split())
    if x - 2 >= 0:
        a[x - 2] += y - 1
    if x < n:
        a[x] += a[x - 1] - y
    a[x - 1] = 0
for i in a:
    print(i)

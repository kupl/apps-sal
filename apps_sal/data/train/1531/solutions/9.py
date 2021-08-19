n = int(input())
a = list(map(int, input().split()))
m = int(input())
for _ in range(m):
    (x, y) = map(int, input().split())
    x -= 1
    if x - 1 >= 0:
        a[x - 1] += y - 1
    if x + 1 < n:
        a[x + 1] += a[x] - y
    a[x] = 0
print(*a, sep='\n')

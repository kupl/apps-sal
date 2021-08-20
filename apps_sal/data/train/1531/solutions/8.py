n = int(input())
a = list(map(int, input().split()))
m = int(input())
mini = 0
maxi = n - 1
for i in range(m):
    (x, y) = list(map(int, input().split()))
    x = x - 1
    left = y - 1
    right = a[x] - left - 1
    if x - 1 >= 0:
        a[x - 1] += left
    if x + 1 <= n - 1:
        a[x + 1] += right
    a[x] = 0
for i in range(len(a)):
    print(a[i])

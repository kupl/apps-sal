(m, n) = [int(i) for i in input().split()]
a = []
for i in range(0, m):
    x = [int(j) for j in input().split()]
    a.append(x)
t = int(input())
for ctr in range(0, t):
    sum = 0
    (x1, y1, x2, y2) = [int(i) - 1 for i in input().split()]
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            sum += a[i][j]
    print(sum)

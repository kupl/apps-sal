rows, columns = map(int, input().split())
a = [[0 for j in range(columns + 1)] for i in range(rows + 1)]
for i in range(1, rows + 1):
    x = [int(i) for i in input().split()]
    s = 0
    for j in range(columns):
        s += x[j]
        a[i][j + 1] = s + a[i - 1][j + 1]
for i in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    s = a[x2][y2] - a[x2][y1 - 1] - a[x1 - 1][y2] + a[x1 - 1][y1 - 1]
    print(s)

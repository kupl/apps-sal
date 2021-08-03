t = int(input())
for sai in range(t):
    n, m = [int(x) for x in input().split()]
    a = []
    for i in range(n):
        a.append(input().split())
    for i in range(n):
        for j in range(n):
            if(a[i][j] == 'a'):
                a[i][j] = [1, -1]
            else:
                a[i][j] = [0, -1]
    a[0][0][1] = 1
    for i in range(1, n):
        a[0][i][0] = a[0][i - 1][0] + a[0][i][0]
        a[0][i][1] = a[0][i - 1][1] + 1
    for i in range(1, n):
        a[i][0][0] = a[i - 1][0][0] + a[i][0][0]
        a[i][0][1] = a[i - 1][0][1] + 1

    for i in range(1, n):
        for j in range(1, n):
            if(a[i - 1][j][0] > a[i][j - 1][0]):
                a[i][j][0] = a[i - 1][j][0] + a[i][j][0]
                a[i][j][1] = a[i - 1][j][1] + 1
            else:
                a[i][j][0] = a[i][j - 1][0] + a[i][j][0]
                a[i][j][1] = a[i][j - 1][1] + 1
    for i in range(m):
        p, q = [int(x) for x in input().split()]
        print(a[p - 1][q - 1][1] - a[p - 1][q - 1][0])

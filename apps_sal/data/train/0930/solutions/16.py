for _ in range(int(input())):
    n = int(input())
    l = [[0 for i in range(n)]for i in range(n)]
    l[0][0] = 1
    for i in range(1, n):
        l[0][i] = l[0][i - 1] + i
    for i in range(1, n):
        for j in range(n):
            if j == n - 1:
                l[i][j] = l[i][j - 1] + n - i
            else:
                l[i][j] = l[i - 1][j + 1] + 1
    for i in range(n):
        for j in range(n):
            print(l[i][j], end=" ")
        print()

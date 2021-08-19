for g in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    up = [[0 for i in range(n)] for j in range(2)]
    up[0][n - 1] = 1
    up[1][n - 1] = 1
    for i in range(n - 2, -1, -1):
        if a[i] < a[i + 1]:
            up[0][i] = up[1][i + 1] + 1
            up[1][i] = 1
        elif a[i] > a[i + 1]:
            up[1][i] = up[0][i + 1] + 1
            up[0][i] = 1
        else:
            up[0][i] = up[1][i + 1] + 1
            up[1][i] = up[0][i + 1] + 1
    max1 = 0
    for i in range(n):
        op = up[0][i]
        if i + op >= n:
            max1 = max(max1, op + 1)
        elif op % 2 == 0:
            max1 = max(max1, up[0][i] + 1 + up[1][i + op])
        elif op % 2 == 1:
            max1 = max(max1, up[0][i] + 1 + up[0][i + op])
        max1 = max(max1, up[1][i] + 1)
    print(max1)

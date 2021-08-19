for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a1 = [list((0 for _ in range(n + 1))) for __ in range(n + 1)]
    a2 = [list((0 for _ in range(n + 1))) for __ in range(n + 1)]
    for i in range(n):
        a1[i][i] = a[i]
        a2[i][i] = 0
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            a1[i][j] = 0.5 * (a[i] + a2[i + 1][j]) + 0.5 * (a[j] + a2[i][j - 1])
            a2[i][j] = 0.5 * a1[i + 1][j] + 0.5 * a1[i][j - 1]
    print(a1[0][n - 1])

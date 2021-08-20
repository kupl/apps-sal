t = int(input())
for _ in range(t):
    n = int(input())
    k = n // 2 + 1
    ans = [[' ' for i in range(k)] for j in range(n)]
    for i in range(k):
        ans[i][i] = '*'
    c = k - 2
    for i in range(k, n):
        ans[i][c] = '*'
        c -= 1
    for i in range(n):
        for j in range(k):
            print(ans[i][j], end=' ')
        print()

for _ in range(int(input())):
    s = str(input())
    k = s[::-1]
    n = len(s)
    grid = [[0] * (n + 1) for i in range(n + 1)]
    for i in range(n + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                grid[i][j] = 0
            elif s[i - 1] == k[j - 1]:
                grid[i][j] = grid[i - 1][j - 1] + 1
            else:
                grid[i][j] = max(grid[i - 1][j], grid[i][j - 1])
    if n - grid[n][n] <= 1:
        print("YES")
    else:
        print("NO")

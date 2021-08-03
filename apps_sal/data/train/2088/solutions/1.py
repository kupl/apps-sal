def main():
    n, l = int(input()), list(map(int, input().split()))
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for i in range(n - 1, 0, -1):
        ci, row = l[i - 1], dp[i]
        for j in range(i, n):
            tmp = [1 + row[j]]
            if ci == l[i]:
                tmp.append(1 + dp[i + 1][j] if i + 1 < n else 1)
            for k in range(i + 1, j):
                if ci == l[k]:
                    tmp.append(row[k - 1] + dp[k + 1][j])
            if ci == l[j] and j > i:
                tmp.append(row[j - 1])
            dp[i - 1][j] = min(tmp)
    print(dp[0][n - 1])


def __starting_point():
    main()


__starting_point()

dp = []


def calculate(i, j, colors):
    if i > j:
        return 0
    if dp[i][j] == -1:
        if i == j:
            return 1
        dp[i][j] = 10000
        dp[i][j] = min(dp[i][j], 1 + calculate(i + 1, j, colors))
        # print(i,j)
        if colors[i] == colors[i + 1]:
            dp[i][j] = min(dp[i][j], 1 + calculate(i + 2, j, colors))
        for k in range(i + 2, j + 1):
            if colors[k] == colors[i]:
                dp[i][j] = min(dp[i][j], calculate(i + 1, k - 1, colors) + calculate(k + 1, j, colors))
    return dp[i][j]


def solve():
    t = int(input())
    colors = list(map(int, input().split()))
    [dp.append([-1] * len(colors)) for x in range(len(colors))]
    print(calculate(0, len(colors) - 1, colors))


try:
    solve()
except Exception as e:
    print(e)

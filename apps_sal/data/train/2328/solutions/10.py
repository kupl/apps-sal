def solve(w, sum):
    n = len(w)
    dp = []
    for i in range(n + 1):
        dp.append([0] * (sum + 1))
    for i in range(1, sum + 1):
        dp[0][i] = 0
    for i in range(n + 1):
        dp[i][0] = 1
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            dp[i][j] = dp[i - 1][j]
            if dp[i][j] == 0 and j >= w[i - 1]:
                dp[i][j] = dp[i - 1][j - w[i - 1]]
    return dp[n][sum]


n, q = list(map(int, input().split()))
w = list(map(int, input().split()))
for i in range(q):
    s = list(map(int, input().split()))
    if s[0] == 1:
        w[s[1] - 1] = s[2]
    elif s[0] == 2:
        w = w[:s[1] - 1] + w[s[1] - 1:s[2]][::-1] + w[s[2]:]
    else:
        if(solve(w[s[1] - 1:s[2]], s[3]) == 1):
            print("Yes")
        else:
            print("No")

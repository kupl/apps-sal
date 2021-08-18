n = int(input())
out = [0]
dp = [[float("-inf"), float("-inf"), float("-inf")]]
for _ in range(n):
    x = list(map(int, input().split()))
    x = [x[0] - x[1], x[0], x[0] + x[1]]
    dp.append(x)
dp.append([float("inf"), float("inf"), float("inf")])
for i in range(1, len(dp) - 1):
    if dp[i - 1][2] < dp[i][0]:
        dp[i][2] = dp[i][1]
        out.append(out[-1] + 1)
    elif dp[i][2] < dp[i + 1][1]:
        out.append(out[-1] + 1)
    else:
        dp[i] = [dp[i][1], dp[i][1], dp[i][1]]
        out.append(out[-1])
print(out[-1])

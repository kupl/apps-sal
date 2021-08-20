n = int(input())
arr = [int(x) for x in input().split()]


def solve(i, k):
    if i < 0:
        return 0
    ans = 0
    if dp[i][k] != None:
        return dp[i][k]
    if k == 2:
        ans = max(ans, solve(i - 1, k))
        ans = max(ans, solve(i - 1, k - 1) + arr[i])
    elif k == 1:
        ans = max(ans, solve(i - 1, k - 1) + arr[i])
        ans = max(ans, solve(i - 1, 2))
    else:
        ans = max(ans, solve(i - 1, 2))
    dp[i][k] = ans
    return ans


dp = [[None, None, None] for x in range(n)]
for i in range(n):
    solve(i, 2)
print(dp[-1][-1])

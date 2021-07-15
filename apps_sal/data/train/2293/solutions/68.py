N = int(input())
As = [(A << 20) + i for i, A in enumerate(map(int, input().split()))]


def chmax(i, elem):
    nonlocal dp
    if dp[0][i] < elem:
        dp[1][i] = dp[0][i]
        dp[0][i] = elem
        return True
    elif dp[1][i] < elem < dp[0][i]:  # skip dp[0][i] == elem
        dp[1][i] = elem
        return True
    else:
        return False


dp = [[0] * len(As) for _ in range(2)]  # first largest and second largest
dp[0][0] = As[0]
ans = 0
for i in range(1, 2 ** N):
    for j in range(N):
        if i & (1 << j):
            if chmax(i, dp[0][i & ~(1 << j)]):
                chmax(i, dp[1][i & ~(1 << j)])
    chmax(i, As[i])
    ans = max(ans, (dp[0][i] + dp[1][i]) >> 20)
    print(ans)


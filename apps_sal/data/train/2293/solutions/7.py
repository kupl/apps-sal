import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [[A[i], -1] for i in range(1 << N)]

for i in range(N):
    bit = 1 << i

    for S in range(1 << N):
        if S & bit:
            l = [dp[S][0], dp[S][1], dp[S ^ bit][0], dp[S ^ bit][1]]
            l.sort()
            dp[S][0] = l[-1]
            dp[S][1] = l[-2]

ans = [-1] * (1 << N)

for S in range(1, 1 << N):
    ans[S] = dp[S][0] + dp[S][1]

    if S >= 2:
        ans[S] = max(ans[S], ans[S - 1])

for ans_i in ans[1:]:
    print(ans_i)

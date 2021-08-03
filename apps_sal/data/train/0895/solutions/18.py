def solve(array):
    N = len(array)
    dp = [array[0], array[1]]
    for i in range(2, N):
        dp.append(array[i] + min(dp[i - 2], dp[i - 1]))
    return dp[N - 1]


N = int(input())
costs = list(map(int, input().split()))

if N == 1:
    print(0)
elif N == 2:
    print(min(costs))
else:
    print(min(solve(costs), solve(costs[-1::-1])))

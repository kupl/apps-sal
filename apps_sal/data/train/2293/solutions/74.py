from sys import stdin
readline = stdin.readline

n = int(readline())

a = list(map(int, readline().split()))
k_max = 1 << n

dp = [[a[i], 0] for i in range(k_max)]
for i in range(n):
    bit = (1 << i)
    for src in range(k_max):
        if bit & src:
            continue
        dst = bit | src
        max_values = dp[dst] + dp[src]
        max_values.sort()
        dp[dst] = [max_values[-1], max_values[-2]]

ans = 0
for k in range(1, k_max):
    ans = max(ans, dp[k][0] + dp[k][1])
    print(ans)

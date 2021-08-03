n = int(input())
a = list(map(int, input().split()))

dp = [[0 for _ in range(1 << 20)] for _ in range(2)]
dp[1][0] = 1
xor = 0
ret = 0
for i in range(n):
    xor ^= a[i]
    ret += dp[i & 1][xor]
    dp[i & 1][xor] += 1
print(ret)

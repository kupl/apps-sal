import sys
def read(): return sys.stdin.readline().strip()


n = int(read())
nums = list(map(int, read().split()))
dp = [0] * n
dp[0] = nums[0]
dp[1] = nums[1]
dp[2] = nums[2]
s = sum(nums)
for i in range(2, n):
    dp[i] = min(dp[i - 1], dp[i - 2], dp[i - 3]) + nums[i]

print(s - min(dp[-1], dp[-2], dp[-3]))

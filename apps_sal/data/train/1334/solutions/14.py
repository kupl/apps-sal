# cook your dish here
import sys
input = sys.stdin.readline
n = int(input())
l = input().split()
li = [int(i) for i in l]
dp = [0 for i in range(n)]
if(n <= 3):
    print(0)
    return
dp[0] = li[0]
dp[1] = li[1]
dp[2] = li[2]
for i in range(3, n):
    dp[i] = li[i] + min(dp[i - 1], dp[i - 2], dp[i - 3])
print(min(dp[n - 1], dp[n - 2], dp[n - 3]))

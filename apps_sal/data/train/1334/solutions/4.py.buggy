# cook your dish here
n = int(input())
arr = list(map(int, input().split()))
i = 0
if(n < 3):
    print(0)
    return
dp = [n for n in arr]
for i in range(3, n):
    dp[i] = arr[i] + min(dp[i - 1], dp[i - 2], dp[i - 3])
print(min(dp[-1], dp[-2], dp[-3]))

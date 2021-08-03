n = int(input())
arr = list(map(int, input().split()))
# if(n==1):
#     print(arr[-1])
# elif(n==2):
#     print(min(arr))
# else:
if(n > 0):
    dp = [0 for i in range(n)]
    dp[0] = arr[0]
    dp[1] = arr[1]
    for i in range(2, n):
        dp[i] = arr[i] + min(dp[i - 1], dp[i - 2])
    comp = (dp[-1])
    dp[1] += dp[0]
    for i in range(2, n - 1):
        dp[i] = arr[i] + min(dp[i - 1], dp[i - 2])
    print(min(comp, dp[n - 2]))


# [3,2,3,4,5,5]
# [3,2,1,2,2,1]

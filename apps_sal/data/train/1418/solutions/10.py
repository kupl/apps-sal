# cook your dish here
for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    dp = [0 for i in range(n + 1)]

    dp[1] = a[0]
    # print(dp)
    for i in range(2, n + 1):
        dp[i] = max(dp[i - 2] + a[i - 2] * (i) + a[i - 1] * (i - 1), dp[i - 1] + a[i - 1] * (i))
        #print('Pass {}: {}'.format(i,dp))
    print(dp[n])

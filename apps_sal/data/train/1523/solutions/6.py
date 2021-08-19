n = int(input())
ipl = list(map(int, input().split()))
dp = list()
for i in range(1, n + 1):
    dp.append(0)
if n == 1:
    print(ipl[0])
elif n == 2:
    print(ipl[0] + ipl[1])
elif n == 3:
    print(max(ipl[0] + ipl[1], max(ipl[0] + ipl[2], ipl[1] + ipl[2])))
else:
    summ = 0
    for i in range(0, n):
        summ += ipl[i]
    dp[0] = ipl[0]
    dp[1] = ipl[1]
    dp[2] = ipl[2]
    for i in range(3, n):
        dp[i] = ipl[i] + min(dp[i - 1], min(dp[i - 2], dp[i - 3]))
    print(summ - min(dp[n - 1], min(dp[n - 2], dp[n - 3])))

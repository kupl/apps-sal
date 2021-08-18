t = int(input())
while t:
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    dp = [a[0]]
    cnt = 0
    value, rang = dict(), dict()
    value[dp[0]] = 0
    rang[dp[0]] = 0
    for i in range(1, n):
        dp.append(dp[i - 1] ^ a[i])
        value[dp[i]] = 0
        rang[dp[i]] = 0

    for i in range(n):
        if value[dp[i]] > 0:
            if dp[i] == 0:
                cnt += i
                cnt += (i - 1) * value[dp[i]] - rang[dp[i]]
                value[dp[i]] += 1
                rang[dp[i]] += i
            else:
                cnt += (i - 1) * value[dp[i]] - rang[dp[i]]
                value[dp[i]] += 1
                rang[dp[i]] += i

        else:
            if dp[i] == 0:
                cnt += i
            value[dp[i]] += 1
            rang[dp[i]] += i

    print(cnt)

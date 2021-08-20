t = int(input())
for k in range(t):
    s = input().strip()
    n = len(s)
    dp = [0]
    for i in s:
        if i == '1':
            dp.append(dp[-1] + 1)
        else:
            dp.append(dp[-1])
    d = 1
    ans = 0
    l = d * d + d
    while l <= n:
        i = 0
        while i <= n - l:
            j = i + l
            cnt1 = dp[j] - dp[i]
            if cnt1 == d:
                ans += 1
                i += 1
            else:
                i += abs(d - cnt1)
        d += 1
        l = d * d + d
    print(ans)

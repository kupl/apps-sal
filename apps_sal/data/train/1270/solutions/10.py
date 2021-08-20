for _ in range(int(input())):
    (n, k) = map(int, input().split())
    h = list(map(int, input().split()))
    h.sort(reverse=True)
    h1 = []
    summ = 0
    for i in range(n):
        summ += h[i]
        h1.append(summ)
    dp = []
    ele = [200000] * (k + 1)
    dp.append(ele)
    for i in range(n):
        ele = [0] * (k + 1)
        dp.append(ele)
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if h[i - 1] >= j:
                dp[i][j] = h[i - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], h[i - 1] + dp[i - 1][j - h[i - 1]])
    i = 1
    while i <= n:
        if h1[i - 1] - dp[i][k] >= k:
            break
        else:
            i += 1
    if i > n:
        print(-1)
    else:
        print(i)

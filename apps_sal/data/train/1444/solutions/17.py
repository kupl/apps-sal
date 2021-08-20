for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    dp = [0] * (n + 3)
    dp[0] = 1
    for i in range(1, n):
        dp[i] = dp[i - 1]
        if i - 2 >= 0 and a[i - 2] == 2:
            dp[i] += dp[i - 2]
        if i - 3 >= 0 and a[i - 3] == 2 and (a[i - 2] == 2):
            dp[i] += dp[i - 3]
    dpr = [0] * (n + 3)
    i1 = [0] * n
    i2 = -1
    for i in range(n - 1, -1, -1):
        i1[i] = i2
        if a[i] == 1:
            i2 = i
    for i in range(1, n - 1):
        if a[i - 1] == 1:
            continue
        if i1[i] == -1:
            i2 = n - i - 1
            if i2 % 2:
                z = 2 * (i2 // 2) + 1
            else:
                z = i2
        else:
            i2 = i1[i] - i - 1
            if not i2 % 2:
                z = i2 + 1
                if i1[i] + 1 < n and a[i1[i] + 1] == 2:
                    z += 1
            else:
                z = 2 * (i2 // 2) + 1
        dpr[i] = z * dp[i - 1]
    c = 0
    for i in range(n):
        c += dp[i] + dpr[i]
    x = 7 + pow(10, 9)
    print(c % x)

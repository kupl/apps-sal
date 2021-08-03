for _ in range(int(input())):
    num = int(input())
    arr = list(map(int, input().split()))
    dp = [0] * num
    dpr = [0] * num
    dpt = [0] * num
    dp[0] = 1
    dpr[0] = 0
    ans = 1
    j = 0
    for i in range(1, num):
        dp[i] = dp[i - 1] % 1000000007
        if i - 2 >= 0 and arr[i - 2] == 2:
            dp[i] += dp[i - 2] % 1000000007
            if i - 3 >= 0 and arr[i - 3] == 2:
                dp[i] += dp[i - 3] % 1000000007
        if arr[i - 1] == 2 and i < num - 1:
            if i >= j or j == 0:
                j = i + 1
                while j < num and arr[j] == 2:
                    j += 1
            count = j - i
            if j == num:
                dpr[i] = dp[i - 1] * (count - 1) % 1000000007
            elif count % 2 != 0:
                if j < num - 1 and arr[j + 1] == 2:
                    dpr[i] = dp[i - 1] * (count + 1) % 1000000007
                else:
                    dpr[i] = dp[i - 1] * (count) % 1000000007
            elif count % 2 == 0:
                dpr[i] = dp[i - 1] * (count - 1) % 1000000007
        ans += (dpr[i] + dp[i]) % 1000000007
    print(ans % 1000000007)

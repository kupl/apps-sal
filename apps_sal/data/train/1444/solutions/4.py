for _ in range(int(input())):
    num = int(input())
    arr = list(map(int, input().split()))
    dp = [0] * num
    dp[0] = 1
    ans = 1
    for i in range(1, num):
        j = i + 1
        count = 1
        dp[i] = dp[i - 1]
        if i - 2 >= 0 and arr[i - 2] == 2:
            dp[i] += dp[i - 2]
            if i - 3 >= 0 and arr[i - 3] == 2:
                dp[i] += dp[i - 3]
        ans += dp[i] % 1000000007
        if arr[i - 1] == 2 and i < num - 1:
            while j < len(arr) and arr[j] == 2:
                j += 1
                count += 1
            if j == num:
                ans += dp[i - 1] * (count - 1) % 1000000007
            elif count % 2 != 0:
                if j < num - 1 and arr[j + 1] == 2:
                    ans += dp[i - 1] * (count + 1) % 1000000007
                else:
                    ans += dp[i - 1] * (count) % 1000000007
            elif count % 2 == 0:
                ans += dp[i - 1] * (count - 1) % 1000000007
    print(ans)

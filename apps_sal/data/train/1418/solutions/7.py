# cook your dish here
for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().rstrip().split()))
    dp = [0] * (n + 1)

    for i in range(n + 1):
        if i == 0:
            dp[i] = 0
        elif i == 1:
            dp[i] = l[i - 1]
        else:
            # dekho swap kare ya nahi but prev wala
            dp[i] = max(dp[i - 1] + l[i - 1] * i, dp[i - 2] + l[i - 1] * (i - 1) + l[i - 2] * i)

    print(dp[n])

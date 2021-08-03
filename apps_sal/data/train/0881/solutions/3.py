t = int(input())
for _ in range(t):
    a = int(input())
    lst = list(map(int, input().split()))
    dp = [1] * a
    count = 1
    for i in range(a - 2, -1, -1):
        if lst[i] <= lst[i + 1]:
            dp[i] = dp[i + 1] + 1
        count += dp[i]
    print(count)  # cook your dish here

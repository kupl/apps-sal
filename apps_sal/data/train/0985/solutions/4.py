# cook your dish here
try:
    x = []
    n = int(input())
    for _ in range(n):
        x.append(int(input()))
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if x[i] % x[j] == 0:
                dp[i] = max(dp[i], dp[j] + 1)
    print(max(dp))
except:
    pass

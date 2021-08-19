t = int(input())
for _ in range(t):
    n = int(input())
    dp = [[0 for i in range(n * 2)] for i in range(n)]
    for i in range(2 * n):
        if i % 2:
            for j in range(n):
                dp[j][i] = j + 1
        else:
            for j in range(n):
                dp[j][i] = i // 2 + 1
    for i in range(n):
        x = ''.join(map(str, dp[i]))
        print(x)

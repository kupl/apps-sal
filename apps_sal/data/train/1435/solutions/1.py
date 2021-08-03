n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
bb = b[:]
for i in range(n):
    b[i] -= 1000
ans = []
dp = []
for i in range(n + 1):
    dp.append([0] * (n + 1))
for offset in range(2001):
    for i in range(n + 1):
        dp[i][0] = 0
        dp[i][0] = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if(a[i - 1] == b[j - 1]):
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    if(dp[n][n] > len(ans)):
        ans = []
        j = n
        i = n
        while(i > 0 and j > 0):
            if(dp[i][j] > dp[i][j - 1] and dp[i][j] > dp[i - 1][j]):
                ans.append([i - 1, j - 1])
                i -= 1
                j -= 1
            elif(dp[i][j] > dp[i][j - 1]):
                i -= 1
            else:
                j -= 1
    for i in range(n):
        b[i] += 1
print(len(ans))
printable = [[], []]
for i, j in ans[::-1]:
    printable[0].append(a[i])
    printable[1].append(bb[j])
print(*printable[0])
print(*printable[1])

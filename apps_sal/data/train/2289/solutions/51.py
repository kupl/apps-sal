def calcNext(s):
    n = len(s)
    res = [[n + 1] * 26 for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(26):
            res[i][j] = res[i + 1][j]
        res[i][ord(s[i]) - ord('a')] = i
    return res


def solve(s):
    n = len(s)
    nx = calcNext(s)
    dp = [n + 1] * (n + 1)
    recon = ['a'] * (n + 1)
    dp[n] = 1
    for i in range(n - 1, -1, -1):
        for j in range(26):
            if nx[i][j] == n + 1:
                if dp[i] > 1:
                    dp[i] = 1
                    recon[i] = chr(ord('a') + j)
            else:
                if dp[nx[i][j] + 1] + 1 < dp[i]:
                    dp[i] = dp[nx[i][j] + 1] + 1
                    recon[i] = chr(ord('a') + j)
    res = ''
    idx = 0
    while idx <= n:
        res += recon[idx]
        idx = nx[idx][ord(recon[idx]) - ord('a')] + 1
    return res


S = input()
print(solve(S))

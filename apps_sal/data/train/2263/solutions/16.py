def main():
    md = 998244353
    s = input()
    n = len(s)
    if s.count(s[0]) == n:
        print(1)
        return
    if n == 2:
        print(2)
        return
    if n == 3:
        if s[0] == s[-1]:
            print(7)
        elif s[0] == s[1] or s[1] == s[2]:
            print(6)
        else:
            print(3)
        return
    ord0 = ord('a')
    a = [ord(c) - ord0 for c in s]
    r = sum(a) % 3
    dp = [[[[0] * 3 for _ in range(2)] for _ in range(3)] for _ in range(n)]
    for m in range(3):
        dp[0][m][0][m] = 1
    for i in range(n - 1):
        for j in range(3):
            for k in range(2):
                for m in range(3):
                    pre = dp[i][j][k][m]
                    for nm in range(3):
                        nj = (j + nm) % 3
                        if nm == m:
                            dp[i + 1][nj][1][nm] = (dp[i + 1][nj][1][nm] + pre) % md
                        else:
                            dp[i + 1][nj][k][nm] = (dp[i + 1][nj][k][nm] + pre) % md
    d = 1
    for (c0, c1) in zip(s, s[1:]):
        if c0 == c1:
            d = 0
            break
    print((sum(dp[n - 1][r][1]) + d) % md)


main()

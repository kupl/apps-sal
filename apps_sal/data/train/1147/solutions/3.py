try:
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        i, res = 0, 0
        dp = [0] * 26
        for i in range(n):
            dp[ord(s[i]) - 97] += 1
        for i in range(26):
            if(dp[i] % 2 == 1):
                res += 1
        if res > 0:
            res -= 1
        print(res)
except EOFError:
    pass

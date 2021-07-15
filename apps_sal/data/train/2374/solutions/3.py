q = int(input())

I = {'1', '2'}
V = {'3','4','5','6'}

for case in range(q) :
    n = int(input())
    a = ['$'+input(), '$'+input()]

    dp = [ [False for _ in range(1+n)],  [False for _ in range(1+n)] ]

    dp[0][0] = True

    for i in range(1, 1+n) :
        # print(a[0][i], a[1][i] in I)

        if a[0][i] in I : dp[0][i] = dp[0][i-1]
        if a[1][i] in I : dp[1][i] = dp[1][i-1]

        if a[0][i] in V and a[1][i] in V :
            dp[0][i] = dp[0][i] or dp[1][i-1]
            dp[1][i] = dp[1][i] or dp[0][i-1]

    print( "YES" if dp[1][n] else "NO" )


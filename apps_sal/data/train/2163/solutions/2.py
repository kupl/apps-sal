import sys
readline = sys.stdin.readline

MOD = 10**9+7
S = readline().strip().split('1')
if len(S) == 1:
    print(len(S[0]))
else:
    S = [len(s)+1 for s in S]
    ans = S[0]*S[-1]
    S = S[1:-1]
    
    dp = [0]*(max(S)+2)
    dp[0] = 1
    for ai in S:
        res = 0
        rz = 0
        for i in range(ai+1):
            res = (res + dp[i])%MOD
            rz = (rz + (ai-i)*dp[i])%MOD
            dp[i] = 0
        dp[0] = rz
        dp[ai] = res
    aaa = 0
    for d in dp:
        aaa = (aaa+d)%MOD
    print(aaa*ans%MOD)


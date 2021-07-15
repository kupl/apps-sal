def pack_bagpack(scores, weights, capacity):
    dp=[[0,[]] for i in range(capacity+1)]
    for j in range(1,len(scores)+1):
        r = [[0,[]] for i in range(capacity+1)]
        for i in range(1,capacity+1):
            c,p = weights[j-1], scores[j-1]
            if c<=i and p+dp[i-c][0]>dp[i][0]: r[i]=[p+dp[i-c][0], dp[i-c][1]+[j-1]]
            else: r[i]=dp[i]
        dp = r
    return dp[-1][0]

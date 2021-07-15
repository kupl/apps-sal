try:
    def help(a,s): 
          
            dp = [[0 for i in range(len(a))] for j in range(0,s+1)] 
            for i in range(len(a)): 
                dp[0][i] = 1
            for i in range(1,s+1): 
                if i == a[0]: 
                    dp[i][0] = 1
            for i in range(1, s+1): 
                for j in range(1, len(a)): 
                    if a[j]<=i: 
                            dp[i][j] = dp[i][j-1] + dp[i-a[j]][j-1] 
                    else: 
                            dp[i][j] = dp[i][j-1] 
            return dp[s][len(a)-1]
        
    test = int(input())
    for i in range(test):
        no1 = int(input())

        s = int(input())

        a = []

        a = [int(x) for x in input().split()]

        print(help(a,s)) 
except EOFError:
    pass




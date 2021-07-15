from sys import stdin,stdout
for _ in range(1):#(stdin.readline())):
    n=int(stdin.readline())
    # n,m=list(map(int,stdin.readline().split()))
    a=list(map(int,stdin.readline().split()))
    dp=[[0 for _ in range(n)] for _ in range(n)]
    for sz in range(n):
        for i in range(n-sz):
            j=i+sz
            # print(i,j)
            if sz==0:dp[i][j]=1
            elif sz==1:dp[i][j]=1+int(a[i]!=a[j])
            else:
                v=n
                if a[i]==a[j]:v=dp[i+1][j-1]
                for k in range(i,j):
                    v=min(v,dp[i][k]+dp[k+1][j])
                dp[i][j]=v
    # print(*dp,sep='\n')
    print(dp[0][n-1])

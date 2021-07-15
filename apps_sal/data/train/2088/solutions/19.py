from sys import stdin,stdout
for t in range(1):#int(stdin.readline())):
    n=int(stdin.readline())
    a=list(map(int,stdin.readline().split()))
    dp=[[0 for i in range(n)] for _ in range(n)]
    for sz in range(n):
        for i in range(n-sz):
            j=i+sz
            if sz<=1:
                dp[i][j]=1 if a[i]==a[j] else 2
            else:
                v=j-i+1
                for k in range(i,j):
                    v=min(v,dp[i][k]+dp[k+1][j])
                if a[i]==a[j]:v=min(v,dp[i+1][j-1])
                dp[i][j]=v
    print(dp[0][n-1])

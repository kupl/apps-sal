import math,sys
n=int(input())
s=input()
dp=[0]*(n+1)
currlength=0
d=[-1]*(n+1)
for i in range(n):
    if s[i]=='0':
        dp[i+1]=dp[i]
        if currlength>0:
            for j in range(currlength):
                d[j+1]=i-j-1
        currlength=0
    else:
        currlength+=1
        numsegs=i-d[currlength]-1
        dp[i+1]=dp[i]+numsegs+1
print(sum(dp))

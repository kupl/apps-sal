import sys
import math
from collections import defaultdict,deque
s=sys.stdin.readline()[:-1]
n=len(s)
dp=[[False for _ in range(n)] for x in range(n)]
left=[n for _ in range(n)]
ans=0
for i in range(n-1,-1,-1):
    right=i
    for j in range(i+1,n):
        if j-i+1==2:
            if (s[i]=='(' or s[i]=='?') and (s[j]==')' or s[j]=='?'):
                dp[i][j]=True
                left[j]=min(left[j],i)
                right=j
                ans+=1
                continue
        if (j-i+1)%2==0:
            l=left[j]
            if dp[i][l-1]:
                dp[i][j]=True
                left[j]=i
                right=j
                ans+=1
                continue
            if dp[right+1][j]:
                dp[i][j]=True
                left[j]=i
                right=j
                ans+=1
                continue
            if (s[i]=='(' or s[i]=='?') and (s[j]==')' or s[j]=='?'):
                if dp[i+1][j-1]:
                    dp[i][j]=True
                    left[j]=i
                    right=j
                    ans+=1
                    continue
#print(dp,'dp')
'''for i in range(n):
    print(dp[i])'''
print(ans)
            
            


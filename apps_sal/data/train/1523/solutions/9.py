# cook your dish here
import sys
import bisect
input=sys.stdin.readline
n=int(input())
l=input().split()
li=[int(i) for i in l]
if(n<=2):
    print(sum(li))
    return
dp=[0 for i in range(n)]
dp[0]=li[0]
dp[1]=li[0]+li[1]
dp[2]=max(dp[1],li[2]+dp[0],li[1]+li[2])
for i in range(3,n):
    dp[i]=max(dp[i-1],li[i]+dp[i-2],li[i-1]+li[i]+dp[i-3])
print(dp[n-1])


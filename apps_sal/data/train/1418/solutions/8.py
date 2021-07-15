# cook your dish here
for _ in range(int(input())):
 n = int(input())
 a = list(map(int,input().split()))
 dp = [0,a[0]]
 for i in range(2,n+1):
  dp.append(max(dp[i-1]+a[i-1]*i,dp[i-2]+a[i-1]*(i-1)+a[i-2]*(i)))
 print(dp[-1])

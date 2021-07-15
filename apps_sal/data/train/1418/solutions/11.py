for _ in range(int(input())):
 n = int(input())
 a = list(map(int,input().split()))
 dp = [0]*n
 dp[0] = a[0]
 dp[1] = max(dp[0]+a[1]*2,a[1]*1+a[0]*2)
 for i in range(2,n):
  dp[i] = max(dp[i-1]+a[i]*(i+1), dp[i-2]+a[i-1]*(i+1)+a[i]*i)
 print(dp[-1])

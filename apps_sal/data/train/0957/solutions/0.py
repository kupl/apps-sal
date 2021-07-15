n = int(input())
for i in range(n) :
 t = int(input())
 li = sorted(list(map(int , input().split())))
 ans = 1
 dp = [li[1]-li[0]] + [0] * (t-2) + [li[t-1] - li[t-2]]
 for i in range(1 , t-1) :
  dp[i] = min(li[i] - li[i-1] , li[i+1] - li[i])
 print(max(dp))


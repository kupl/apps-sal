n = int(input().strip())
l = [int(x) for x in input().strip().split()]
k = int(input().strip())

dp = [0]*n
dp[0]=l[0]

for i in range(1,n):
    dp[i]=dp[i-1]+l[i]

maxo=0

if(k==n):
    print(dp[n-1])
    return
for i in range(k+1):# 0 to k elements from the start
    if(i==0):
        cur=dp[n-1]-dp[n-k-1]
    else:
        cur=dp[n-1]-dp[n-k-1 + i]  + dp[i-1]
    maxo = max(maxo,cur)
print(maxo)



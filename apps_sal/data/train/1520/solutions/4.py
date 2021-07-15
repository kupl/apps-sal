n=int(input())
l=list(map(int,input().split()))
a=[]
for i in range(0,n):
    for j in range(i+1,n):
     a.append((l[i]^l[j],(i,j)))

a.sort()
dp=[0]*n
for i in range(0,len(a)):
    x=a[i][0]
    left,right=a[i][1][0],a[i][1][1]
    dp[right]=max(dp[left]+1,dp[right])

print(max(dp)+1)

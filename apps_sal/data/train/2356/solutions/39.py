n,k = map(int,input().split())
a = [[0]*(n+1) for i in range(n+1)]
for i in range(1,n+1):
  for j in range(i,0,-1):
    if i==j:
      a[i][j] = 1
    elif j>0:
      a[i][j] = a[i-1][j-1]
      if i>=2*j:
        a[i][j] += a[i][2*j]
        a[i][j] %= 998244353
print(a[n][k])

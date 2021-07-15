def fast_ncr(n,r):
 res = 1
 for i in range(1,r+1):
  res*=(n-r+i)
  res/=(i)
 return res

def fast_exp(base,e):
 res = 1
 while (e>0):
  if (e%2==1):
   res = res*base%1000000007
  base = base*base%1000000007
  e/=2
 return (res)%1000000007
 
for t in range(int(input())):
 n,q = list(map(int, input().split()))
 for Q in range(q):
  i, j = list(map(int,input().split()))
  i-=1
  j-=1
  if (i<j):
   print(0)
  else:
   print((fast_ncr(i,j) * fast_exp(2,(n-i-1)))%1000000007)

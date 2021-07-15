def comb(n,m):
  p=10**9+7
  
  inv=[0]*(m+1)
  finv=[0]*(m+1)
  inv[1]=1
  finv[0]=1
  finv[1]=1
  for i in range(2,m+1):
    inv[i]=(-(p//i)*inv[p%i])%p
    finv[i]=finv[i-1]*inv[i]%p
  
  if m>n:
    return 0
  elif n<0 or m<0:
    return 0
  else:
    #print(inv)
    #print(finv)
    ans=1
    for i in range(n,n-m,-1):
      ans=(ans*i)%p
      
    return (ans*finv[m])%p
  
n,m=list(map(int,input().split()))
a=list(map(int,input().split()))
s=sum(a)
print((comb(m+n,s+n)))



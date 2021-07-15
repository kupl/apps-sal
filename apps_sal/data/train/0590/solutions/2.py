def modInverse(a, m) : 
 m0 = m 
 y = 0
 x = 1

 if (m == 1) : 
  return 0

 while (a > 1) : 
  q = a // m 

  t = m 
  m = a % m 
  a = t 
  t = y 
  y = x - q * y 
  x = t 
 if (x < 0) : 
  x = x + m0 

 return x
p=10**9+7
f=[1]*(100000+1)
for i in range(1,100000+1):
 f[i]=i*f[i-1]
 if f[i]>p:
  f[i]=f[i]%p

for _ in range(int(input())):
 n,x,m=map(int,input().split( ))
 m=m%p
 a=list(map(int,input().split( ))) 
 pre=[1]*(x)
 for i in range(1,x):
  pre[i]=pre[i-1]*((m+(i-1)))*f[i-1]
  inv=modInverse(f[i],p)
  pre[i]=(pre[i]*inv)%p
 ans=0
 j=0 
 for i in range(x-1,-1,-1):
  ans+=a[j]*pre[i]
  if ans>p:
   ans=ans%p
  j+=1
 print(ans%p)

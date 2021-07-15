def ncr(n, r, p): 
 num = den = 1 
 for i in range(r): 
  num = (num * (n - i)) % p 
  den = (den * (i + 1)) % p 
 return (num * pow(den, p - 2, p)) % p 
a,b=map(int,input().split())
m=10**9+7
print(ncr(a+b-1,b,m))

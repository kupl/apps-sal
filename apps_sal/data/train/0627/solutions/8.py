# Python3 function to 
# calculate nCr % p 
def ncr(n, r, p): 
 # initialize numerator 
 # and denominator 
 num = den = 1
 for i in range(r): 
  num = (num * (n - i)) % p 
  den = (den * (i + 1)) % p 
 return (num * pow(den, 
   p - 2, p)) % p 
M=10**9+7
N,K=map(int,input().split())
ans=0
for i in range(N,0,-1):
 ans+=ncr(N-i+K-1,K-1,M)
 ans%=M
print(ans) 

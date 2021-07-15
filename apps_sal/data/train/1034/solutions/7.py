def factorizing(n):
 factor = []
 for i in range(2,int(n**0.5)+1):
  if n%i==0:
   count = 0
   while n%i==0:
    count += 1
    n //= i
   factor.append(i**count)
 
 if (n!=1):
  factor.append(n)
 return factor


def getans(a,f,p):
 if p==len(f):
  return sum(a)
 
 ans = float('inf')
 
 for i in range(len(a)):
  a[i] *= f[p]
  ans = min(ans,getans(a,f,p+1))
  a[i] //= f[p]
 
 return ans

T = int(input())

while(T):
 
 T -= 1
 
 k,x = map(int, input().split())
 
 factors = factorizing(x)
 
 if len(factors)<=k:
  ans = sum(factors) + k-len(factors)
 else:
  a = [1]*k
  ans = getans(a,factors, 0)
 
 print(ans)

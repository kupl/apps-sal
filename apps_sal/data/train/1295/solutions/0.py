mod=10**9+7
def fibonacci(n):
 if n < 0:
  raise ValueError("Negative arguments not implemented")
 return (_fib(n)[0]%mod + mod)%mod;
def _fib(n):
 if n == 0:
  return (0, 1)
 else:
  a, b = _fib(n // 2)
  c = (a * (b * 2 - a))%mod
  d = (a * a + b * b)%mod
  if n % 2 == 0:
   return (c, d)
  else:
   return (d, c + d)
def inv(n):
 return pow(n,mod-2,mod)
def brute(n,k):
 ret = 0
 for i in range(0,n+1):
  ret+=fibonacci(i)*pow(k,i,mod)
 return ret%mod
def ans(n,k):
 k%=mod
 a = pow(k,n+1,mod)
 b=(a*k)%mod
 x = a*(fibonacci(n+1))+b*fibonacci(n)-k
 y = inv((k*k+k-1)%mod)
 return ((x*y)%mod+mod)%mod
for t in range(0,eval(input())):
 n,k = list(map(int,input().split()))
 print(ans(n,k))

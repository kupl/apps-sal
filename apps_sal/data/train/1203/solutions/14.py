fact = [1]

def factorial(n):
 l = len(fact)
 i = n - l
 if (i<1):
  i = 0
 for x in range(i+1):
  fact.append(fact[-1]*l)
  l+=1
 return fact[n]
 
def nCr(n,r):
 return (factorial(n) / factorial(r) / factorial(n-r))%1000000007

def fast_exp(base,e):
 res = 1
 while (e>0):
  if (e%2==1):
   res = res*base%1000000007
  base = base*base%1000000007
  e/=2
 return (base*res)%1000000007

for t in range(int(input())):
 n,q = list(map(int, input().split()))
 for Q in range(q):
  i, j = list(map(int,input().split()))
  i-=1
  j-=1
  if (i<j):
   print(0)
  else:
   print((nCr(i,j) * 2**(n-i-1))%1000000007)

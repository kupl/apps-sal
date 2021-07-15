import sys
 
MOD = 1000000000
 
T = int(sys.stdin.readline())
 
 
def gcd(a, b):
 return a if b == 0 else gcd(b, a % b)
 
 
def solve(n, r):
 if r > n - r:
  r = n - r
 
 num = 1
 den = 1
 j = 1
 for i in range(n - r + 1, n + 1):
  num *= i
  den *= j
  j += 1
 
 return (num / den) % MOD
 
for t in range(T):
 n, r = list(map(int, sys.stdin.readline().split()))
 t=r-1
 q=0
 li=[]
 for i in range(r+1):
  li.append(solve(t,q))
  t+=1
  q+=1
 arr=li[:]
 temp=0
 for i in range(1,n):
  summ=sum(arr)
  for j in range(r+1):
   if(j==0):
    summ+=0
   else:
    summ-=temp
   temp=arr[j]
   arr[j]=(li[j]*(summ%MOD))%MOD
 print(sum(arr)%MOD) 

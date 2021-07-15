import sys
z=(10**9+7)

cachencr=[None]*100000000
cachepow=[None]*4000
fact=[]
fact.append(1)

for i in range(1,4000):
 fact.append(i*fact[i-1]%z)

def factorialMod(n):
 ans=1
 for i in range(1,n+1):
  ans = ans * i % z 
 return ans % z
 
def nCr(n,r):
 if r>n:
  return 0
 key = n+(r*10000)
 if cachencr[key]!=None:
  return cachencr[key]
 else:
  cachencr[key]=fact[n]*pow(fact[r]*fact[n - r], z - 2, z) % z
  return cachencr[key]
  
def powc(n):
 if cachepow[n]!=None:
  return cachepow[n]
 else:
  cachepow[n] = pow(2,n,z)
  return cachepow[n]
 
for _ in range(0,int(input())):
 n,q = list(map(int,input().split()))
 for __ in range(0,q):
  i,k= list(map(int,sys.stdin.readline().split()))
  a = nCr(i-1,k-1)
  b = powc(n-i)
  print((a*b)%z)

e=10**9+7

def fact(n):
 ans=1
 for i in range(2,n+1):
  ans=(ans*i)%e
 return ans
  
t=int(input())
for _ in range(t):
 s=input()
 n=len(s)
 d={}
 for i in s:
  try:
   d[i]+=1
  except:
   d[i]=1
 x=fact(n)
 for i in list(d.values()):
  y= fact(i)
  y = pow(y,e-2,e)
  x=(x*y)%e
 print(x)


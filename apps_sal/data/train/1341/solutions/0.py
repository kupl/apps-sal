import bisect

def pre(a):
 for p in range(n-1):
  if(a[p]>=a[p+1]):
   return p
 return n-1 
 
def suf(a):
 for s in range(1,n):
  if(a[n-s]<=a[n-s-1]):
   return n-s
 return 0
 
 

t=int(input())
for _ in range(t):
 n=int(input())
 a=list(map(int,input().split()))
 
 p=pre(a)
 s=suf(a)
 
 b=a[s:n]
 count=0
 for i in range(p+1):
  k=bisect.bisect(b,a[i])
  k+=s
  count+=n-k+1
  
 if(s==0):
  print((n*(n+1))//2-1)
 else:
  print(count+n-s)


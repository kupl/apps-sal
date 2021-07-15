n=int(input())
P=[int(i) for i in input().split()]
import math
import bisect

n_max=2*10**5
nn=int(math.log2(n_max))+1
BIT=[0]*(2**nn+1)

def bitsum(BIT,i):
  s=0
  while i>0:
    s+=BIT[i]
    i-=i&(-i)
  return s
def bitadd(BIT,i,x):
  if i<=0:
    return True
  else:
    while i<=2**nn:
      BIT[i]+=x
      i+=i&(-i)
    return BIT
def bitlowerbound(BIT,s):
  if s<=0:
    return 0
  else:
    ret=0
    k=2**nn
    while k>0:
      if k+ret<=2**nn and BIT[k+ret]<s:
        s-=BIT[k+ret]
        ret+=k
      k//=2
    return ret+1
for i in range(n_max):
  bitadd(BIT,i+1,i+1)

Ans=[]
for i in reversed(range(n)):
  p=P[i]
  ans=bitlowerbound(BIT,p+1)
  Ans.append(ans)
  bitadd(BIT,ans,-ans)
Ans=Ans[::-1]
print(*Ans)

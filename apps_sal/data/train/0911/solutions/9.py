'''
Name : Jaymeet Mehta
codechef id :mj_13
Problem : 
'''
from sys import stdin,stdout
import math
from bisect import bisect_left
mod=1000000007
def mul(a,b):
 nonlocal mod
 return ((a%mod)*(b%mod))%mod
def add(a,b):
 nonlocal mod
 return ((a%mod)+(b%mod))%mod
g=[0,1]
pre=[0,1]
ans=[0,1]
i=2
while(True):
 g.append(1+g[i-g[g[i-1]]])
 pre.append(pre[i-1]+g[i])
 ans.append(add(ans[i-1],mul(mul(i,i),g[i])))
 if pre[i]>10000000000:
  break
 i+=1
test=int(stdin.readline())
for _ in range(test):
 l,r= list(map(int,stdin.readline().split()))
 sm1,sm2=0,0
 
 if l==1:
  sm1=0
 else:
  l-=1
  tl=bisect_left(pre,l)
  sm1=add(ans[tl-1],mul(l-pre[tl-1],mul(tl,tl)))
 tr=bisect_left(pre,r)
 sm2=add(ans[tr-1],mul(r-pre[tr-1],mul(tr,tr)))
 print((sm2-sm1)%mod)


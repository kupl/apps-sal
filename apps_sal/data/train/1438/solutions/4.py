
p=10**6+5
def Sieve():
 l=[True]*p 
 s=[0]*p 
 for i in range(2,p):
  if l[i]:
   for j in range(i,p,i):
    s[j]+=i 
    l[j]=False 
  i+=1 
 l[0]=l[1]=False
 return l,s 
isprime,s=Sieve()
from collections import Counter 
for _ in range(int(input())):
 n=int(input())
 l=[int(i) for i in input().split()]
 c=Counter(l)
 ans=0
 maxi=max(l)
 for i in range(2,maxi+1):
  if c[i]>0:
   for j in range(i,maxi+1,i):
    if s[j]%s[i]==0:
     ans+=c[i]*c[j]
 ans-=n
 print(ans)

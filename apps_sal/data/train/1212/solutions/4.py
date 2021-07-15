# cook your dish here
from collections import Counter
t=int(input())
for i in range(t):
 s=input()
 c=Counter(s)
 l=list(c.values())
 l.sort(reverse=True)
 it=sum(l)
 k=len(l)
 ans=999999999
 while(k>=1):
  if(it%k==0):
   p=it//k
   sumi=0
   for j in range(len(l)):
    if(l[j]>p):
     sumi+=l[j]-p
    else:
     if(j>=k):
      sumi+=l[j]
   if(sumi<ans):
    ans=sumi
  k-=1
 k=len(l)+1
 while(k<=26 and k<=len(s)):
  if(it%k==0):
   p=it//k
   sumi=0
   for j in range(len(l)):
    if(l[j]>p):
     sumi+=l[j]-p
    else:
     break
   if(sumi<ans):
    ans=sumi
  k+=1
 print(ans)


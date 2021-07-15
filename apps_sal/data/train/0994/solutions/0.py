# cook your dish here
import sys
input=sys.stdin.readline
for _ in range(int(input())):
 n,x=list(map(int,input().split()))
 l=[0]
 pre=[0]*(n+1)
 sum=0
 i=1
 for m in input().split():
  l.append(int(m))
  sum+=int(m)
  pre[i]=sum
  i+=1
 dict={}
 k=[]
 i=1
 while (i*i)<=x:
  if x%i==0:
   k.append(i)
   if (i*i)!=x:
    k.append(x//i)
   else:
    break
  i+=1 
 ans=0 
 for a in k:
  if a>n:
   continue
  z=x//a 
  for j in range(a,n+1):
   s=pre[j]-pre[j-a]
   if s>z:
    continue
   if s in dict:
    dict[s]+=1
   else:
    dict[s]=1
  for j in range(a,n+1):
   s=pre[j]-pre[j-a]
   if s>z:
    continue
   if (z-s) in dict:
    ans+=dict[z-s]
  for j in range(a,n+1):
   s=pre[j]-pre[j-a]
   if s>z:
    continue
   dict[s]=0
   
 print(ans) 
   


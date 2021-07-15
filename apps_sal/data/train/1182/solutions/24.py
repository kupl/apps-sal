import sys
sys.setrecursionlimit(10**9)
t=int(input())
prime=[]
ind=2
aa=[-1]*(10**4)
def func(ind,prod):
 nonlocal p,ss,ll
 if ind==len(p) :
  ll.append(prod)
  return ''
 po=prod
 for i in range(p[ind][1]+1):
  #  print(po,i,ind)
  if po>m:
   break
  func(ind+1,po)
  po*=p[ind][0]
 
 
 
while ind<10**4:
 if aa[ind-1]==-1:
  prime.append(ind)
  aa[ind-1::ind]=[0]*len(aa[ind-1::ind])
 ind+=1
 
for _ in range(t):
 m=int(input())
 p=[]
 ind=0
 mm=int(m**0.5)
 n=m
 while prime[ind]<=mm+1:
  count=0
  while True:
   if n%prime[ind]==0:
    count+=2
    n//=prime[ind]
   else:
    break
  if count>0:
   p.append([prime[ind],count])
  ind+=1
 if n!=1:
  p.append([n,2])

 # print(p)
 ss=[]
 ll=[]
 
 func(0,1)
 ll.sort()
 print(len(ll))
 for i in ll:
  print(i+m)
 
   


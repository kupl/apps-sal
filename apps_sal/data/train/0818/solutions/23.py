# cook your dish here
t=int(input())
while t>0:
 t-=1
 n=int(input())
 li=[]
 lis=list(map(int,input().split()))
 for i in range(n):
  if(lis[i]%2==0):
   li.append(i)
 q=int(input())
 for i in range(q):
  l,r=map(int,input().split())
  f=0
  for j in li:
   if(l-1<=j and j<r):
    f=1
    break
   if(j>=r):
    break
  if(f==1):
   print("EVEN")
  else:
   print("ODD")

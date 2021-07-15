# cook your dish here
for _ in range(int(input())):
 n=int(input())
 a=[int(x) for x in input().split()]
 sum=0
 for i in range(n):
  if a[i]%2==0:
   sum+=1
  a[i]=sum 
 q=int(input())
 while q:
  l,r=map(int,input().split())
  if l!=1:
   c=a[r-1]-a[l-2]
  else:
   c=a[r-1] 
  if c==0:
   print("ODD")
  else:
   print("EVEN")
  q-=1

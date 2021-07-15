# cook your dish here
t=int(input())
while t>0:
 n,k=map(int,input().split())
 l=list(input().split())
 l1=l[n-k:]
 c=0
 ch=1
 for i in range(len(l1)-1,-1,-1):
  if l1[i]=='H' and ch==1:
   c+=1
   ch=0
  if l1[i]=='T' and ch==0:
   c+=1
   ch=1
 res=l[0:n-k]
 if c%2==0:
  r=res.count('H')
 else:
  r=res.count('T')
 print(r)
 t-=1

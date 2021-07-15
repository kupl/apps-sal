a=int(input())
for i in range(a):
 n,m=map(int,input().split())
 b=[]
 for j in range(n):
  j=list(input())
  b.append(j)
 c=0
 for k in range(m):
  d=0
  for p in range(n):
   if b[p][k]=='1':
    d+=1
  if d>1:
   c+=((d*(d-1))//2)
 print(c)

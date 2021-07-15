# cook your dish here
for _ in range(int(input())):
 a=[]
 n=int(input())
 for t in range(n):
  p=list(map(int,input().split()))
  a.append(p)
 c=[0]*n
 c[n-1]=max(a[n-1])
 f=0
 s=0
 for i in range(n-2,-1,-1):
  c[i]=0
  for j in range(n):
   if a[i][j]<c[i+1]:
    c[i]=max(c[i],a[i][j])
  if c[i]==0:
   f=1 
   break
  else:
   s+=c[i] 
 
 if f==1:
  print(-1)
 else:
  print(s+c[n-1])


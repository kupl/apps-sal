l=[]
l2=[]
r2=[]
r=[]
a=[]
u=0
q=0
p=0
n = int(input())
for i in range(n):
 x1,x2 = list(map(int, input().split()))
 l.append(x1)
 r.append(x2)
 if x1==0:
     u=u+1   
for i2 in range(u):
 y=0
 for i in range(p,n):
  if l[i]==0 and y==0:
     a.append(i+1)
     y=1
     q=i
     p=i+1
 while r[q]!=0:
    a.append(r[q])
    q=r[q]-1
for i3 in range(n+1):
 l2.append(0)
for i3 in range(1,n):
 l2[a[i3]]=a[i3-1]
del l2[0]


for i3 in range(n+1):
 r2.append(0)
for i3 in range(0,n-1):
 r2[a[i3]]=a[i3+1]
del r2[0]
for i3 in range(n):
    print(l2[i3],r2[i3])


 






t=int(input())
for i0 in range(t):
 n,d=list(map(int,input().strip().split(' ')))
 a=list(map(int,input().strip().split(' ')))
 flag=0
 count=0
 if sum(a)%len(a)!=0:
  flag=1
 else:
  x=sum(a)/len(a)
  for i in range(len(a)-d):
   if flag!=1:
    if a[i]==x:
     pass
    elif a[i]<x:
     j=1
     y=x-a[i]
     while a[i]!=x:
      if a[i+(j*d)]-y>=0:
       a[i]=x
       a[i+(j*d)]-=y
       count+=j*y
       break
      if i+j*d<len(a):
       j+=1
      else:
       flag=1
       break
    else:
     if i+d<len(a):
      count+=a[i]-x
      a[i+d]+=a[i]-x
      a[i]=x
     else:
      flag=1
   else:
    break
 if a.count(x)!=len(a):
  flag=1
 if flag:
  print(-1)
 else:
  print(count) 

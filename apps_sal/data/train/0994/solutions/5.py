import math
for _ in range(int(input())):
 n,x=map(int,input().split())
 a=list(map(int,input().split()))
 count=0
 y=a.copy()
 y.sort()
 for i in range(n):
  if y[i]>=x:
   break
  else:
   p=x-y[i]
   u=0
   v=n-1
   cond=0
   q=0
   while u<=v:
    q=(u+v)//2
    if y[q]>p:
     v=q-1
    elif y[q]<p:
     u=q+1
    else:
     cond=1
     count+=1
     break
   if cond==1:
    r=q
    s=q
    while r>0:
     if y[r-1]==y[r]:
      count+=1
      r-=1
     else:
      break
    while s<n-1:
     if y[s]==y[s+1]:
      count+=1
      s+=1
     else:
      break
 p=math.sqrt(x)
 if n<p:
  p=n
 b=[]
 k=2
 while k<=p:
  if x%k==0:
   b.append(k)
  k+=1
 #print(b)
 for i in b:
  summ=0
  for j in range(i):
   summ+=a[j]
  c=[summ]
  p=0
  for j in range(i,n):
   summ+=a[j]
   summ-=a[p]
   p+=1
   c.append(summ)
  c.sort()
  l=len(c)
  #print(i)
  #print(c)
  for t in range(l):
   if c[t]>=x//i:
    break
   else:
    p=(x//i)-c[t]
    u=0
    v=l-1
    cond=0
    q=0
    while u<=v:
     q=(u+v)//2
     if c[q]>p:
      v=q-1
     elif c[q]<p:
      u=q+1
     else:
      cond=1
      count+=1
      break
    if cond==1:
     r=q
     s=q
     while r>0:
      if c[r-1]==c[r]:
       count+=1
       r-=1
      else:
       break
     while s<l-1:
      if c[s]==c[s+1]:
       count+=1
       s+=1
      else:
       break
    #print(count)
 print(count)

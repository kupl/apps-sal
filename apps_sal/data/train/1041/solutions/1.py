t=int(input())
for i in range(t):
 n=int(input())
 l=[int(x) for x in input().split()]
 s=0
 e=0
 maxi=l[0]
 for i in range(n):
  prod=l[i]
  if prod>maxi:
   maxi=prod
   s=i
   e=i
  if prod==maxi:
   if i>s:
    s=i
    e=i
   if i==s:
    if i>e:
     e=i
  for j in range(i+1,n):
   prod=prod*l[j]
   if prod>maxi:
    maxi=prod
    s=i
    e=j
   if prod==maxi:
    if i>s:
     s=i
     e=j
    if i==s:
     if j>e:
      e=j 
 print(maxi,s,e)

   


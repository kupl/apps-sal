t=eval(input())
author='biggy_bs'
while t>0:
 t-=1
 n,m,z,l,r,b=list(map(int,input().split()))
 max_b=n*((m+1)/2)
 maximm=n*m
 nm=maximm
 answer=0
 if maximm>l+r:
  author=answer
  answer=l+r
  maximm-=(l+r)
  if m%2!=0:
   if maximm<=n-1:
    if b>=maximm:
     maximm-=maximm
    else:
     maximm-=b
   else:
    if b>=(maximm+n)/2:
     maximm-=(maximm+n)/2
    else:
     maximm-=b 
  else:
   author=n*m
   answer=l+r
   if n*m-maximm<=n:
    if b>=max_b:
     maximm-=max_b
    else:
     maximm-=b
   elif maximm<=n-1:
    if b>=maximm:
     maximm-=maximm
    else:
     maximm-=b
   else:
    answer=b
    if b>=(maximm+n)/2:
     maximm-=(maximm+n)/2
    else:
     maximm-=b
  answer=n*m
  if z>=maximm or maximm==0:
   answer=n*m
  else:
   answer=n*m
   answer=n*m-(maximm-z)
  print(answer)
 else:
  nm=n*m
  answer=nm
  print(answer)


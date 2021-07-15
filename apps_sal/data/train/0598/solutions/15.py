n,k=list(map(int,input().split()))
a=list(map(int,input().split()))
b=0
c=110000000
for d in a:
 b=max(b,d)
 c=min(d,c)
if k==0:
 for x in a:
  print(x, end=' ')
else:
 if k%2==0:
  for x in a:
   print(x-c, end=' ')
 else:
  for x in a:
   print(b-x, end=' ')


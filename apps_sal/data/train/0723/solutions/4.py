t=int(input())
st=""
x=0
zt=""
while t:
 t-=1
 n=int(input()) - 1
 a=[int(x) for x in input().split()]
 if a[0] == 0 or a[1]==0:
  x=0
 elif a[1]>1:
  st+=str(a[1]*a[0])+"x^"+str(a[1]-1)
 elif a[1]==1:
  st+=str(a[0])
 while n:
  n-=1
  a=[int(x) for x in input().split()]
  if a[0] == 0 or a[1]==0:
   x=0
  elif a[1]>1:
   st+=" + "+str(a[1]*a[0])+"x^"+str(a[1]-1)
  elif a[1]==1:
   st+=" + "+str(a[0])
 for i in range(len(st)):
  if st[i] == ' ' or st[i] == '+':
   continue
  else:
   break
 st=st[i:]

 print(st)
 st=""




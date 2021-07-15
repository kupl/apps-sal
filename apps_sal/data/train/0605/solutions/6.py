def is_safe(n,m,i,j,s):
 for k in s:
  if(k=='L'):
   j-=1
  if(k=='R'):
   j+=1
  if(k=='U'):
   i-=1
  if(k=='D'):
   i+=1
  if((i<1 or i>n) or (j<1 or j>m)):
   return -1
 return 1
for _ in range(int(input())):
 n,m=[int(x) for x in input().split()]
 s=input()
 flag=0
 l,r,u,d=0,0,0,0
 for i1 in range(1,n+1):
  for i2 in range(1,m+1):
   res=is_safe(n,m,i1,i2,s)
   if res==1:
    flag=1
    break
  else:
   continue
  break

 if(flag==1):
  print("safe")
 else:
  print("unsafe")

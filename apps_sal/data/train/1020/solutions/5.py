for _ in range(int(input())):
 n,k=list(map(int,input().split()))
 l=list(map(int,input().split()))
 x=0
 for i in range(len(l)):
  if i%2==0:
   if x>=0:
    x+=l[i]
   else:
    x-=l[i]
  else:
   if x>=0:
    x-=l[i]
   else:
    x+=l[i]
 if abs(x)>=k:
  print(1)
 else:
  print(2)


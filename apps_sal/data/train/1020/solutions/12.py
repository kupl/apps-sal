for j in range(int(input())):
 n,k=map(int,input().split())
 x=list(map(int,input().split()))
 c=0
 for i in range(n):
  if(i%2==0):
   if(c<0):
    c-=x[i]
   else:
    c+=x[i]
  else:
   if(c<0):
    c+=x[i]
   else:
    c-=x[i]
 if(abs(c)>=k):
  print(1)
 else:
  print(2)

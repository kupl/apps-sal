# cook your dish here
t=int(input())
for i in range(t):
 n,x=list(map(int,input().split()))
 p,l=input().split()
 if(p=="L"):
  if(x%2==1):
   print(x,l)
  else:
   if(l=="H"):
    print(x,"E")
   else:
    print(x,"H")
 else:
  x=n-x+1
  if(x%2==1):
   print(x,l)
  else:
   if(l=="H"):
    print(x,"E")
   else:
    print(x,"H")
    


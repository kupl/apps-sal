# cook your dish here
n=int(input())
for i in range(0,n):
 (l,b)=map(int,input().split(" "))
 lcandie=0
 bcandie=0
 for a in range(1,1000):
  if(a%2==1):
   lcandie+=a
   if(lcandie>l):
    print("Bob")
    break
  else:
   bcandie+=a
   if(bcandie>b):
    print("Limak")
    break

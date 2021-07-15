# cook your dish here# cook your dish here
t=int(input())

for _ in range (t):
 d=int(input())
 s=int(input())
 f=list(map(int,input().split()))
 count=0
 flag=0
 for i in f:
  if(i==1):
   flag= 1
   break
  else:
   flag=0
 if(flag==1):
  print("Impossible")
 else:
  print("Possible")
 


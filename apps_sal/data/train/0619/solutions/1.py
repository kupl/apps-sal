t=int(input())
while t>0:
 p1,p2,k=map(int,input().split())
 s=(p1+p2)//k
 if s%2==0:
  print("CHEF")
 else:
  print("COOK")
 t=t-1

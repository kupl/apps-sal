for _ in range(int(input())):
 ans=0
 c=int(input())
 for i in range(c):
  n,m=list(map(int,input().split( )))
  ans^=(n+m-2)%3
 if not ans:
  print("Football")
 else:
  print("MasterChef")
  


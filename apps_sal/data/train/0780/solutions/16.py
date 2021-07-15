# cook your code here
for _ in range(int(input())):
 n,m=list(map(int,input().split()))
 k=n%m
 if k%2==0:
  print("EVEN")
 else:
  print("ODD")


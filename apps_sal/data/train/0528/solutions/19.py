# cook your dish here
for _ in range(int(input())):
 n,l=map(int,input().split(" "))
 if(n==1):
  print(l)
 if(n==2):
  print((l//n)-1)

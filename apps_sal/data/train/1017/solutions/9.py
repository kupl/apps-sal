# cook your dish here
for i in range(int(input())):
 n=list(map(int,input().split()))
 p=sum(n)-n[-1]
 if p*n[-1]>(5*24):
  print("Yes")
 else:
  print("No")

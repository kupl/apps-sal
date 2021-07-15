n=int(input())
for i in range(n):
 a=list(map(int,input().split()))
 a.sort()
 if a[0]+a[1]>=a[2]-1:
  print("Yes")
 else:
  print("No")
 


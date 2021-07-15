# cook your dish here
for _ in range(int(input())):
 x,y,k,n = map(int,input().split())
 dis = abs(x-y)
 k *= 2
 if dis % k:
  print("No")
 else:
  print("Yes")

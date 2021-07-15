from math import *
for i in range(int(input())):
 num = int(input())
 list1 = list(map(int,input().split()))
 x = list1[0]
 for a in range(1,num):
  x = gcd(x,list1[a])
 if x==1:
  print(num)
 else:
  print(-1)

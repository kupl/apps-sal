# cook your dish here
import math
for h in range(int(input())):
  n=int(input())
  a=math.ceil(n/2)
  a=n-a
  print("1 1",end="")
  for i in range(1,a+1):
   print(0,end="")
  print()

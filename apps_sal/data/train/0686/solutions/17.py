# cook your dish here
import math
for _ in range(int(input())):
 n,v1,v2=map(int,input().split())
 x=(2*n)/v2
 y=(math.sqrt(2)*n)/v1
 if x>y:
  print("Stairs")
 else:
  print("Elevator")

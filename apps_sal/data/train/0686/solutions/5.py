import math
for i in range(int(input())):
 n,v1,v2=list(map(int, input().split()))
 time_stairs=((math.sqrt(2)*n)/v1)
 time_elevator=((2*n)/v2)
 if time_elevator<time_stairs:
  print("Elevator")
 else:
  print("Stairs")
 


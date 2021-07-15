import math
try:
 t = int(input())
 for i in range(t):
  x = list(map(int,input().split()))
  y = x[2]/(math.sqrt(2)*x[1])
  if y>1:
   print("Elevator")
  else:
   print("Stairs")
except:
 pass

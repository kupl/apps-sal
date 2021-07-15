import math
t = int(input())
for i in range(t):
 N,V1,V2=map(int,input().split())
 t1 = (math.sqrt(2) * N)/V1
 t2 = (2*N/V2)

 if(t1<t2):
  print("Stairs")
 else:
  print("Elevator")

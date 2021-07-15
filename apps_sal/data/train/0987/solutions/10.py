import math

t = int(input())

for _ in range(t):
 f, dtb, ta, bs = [int(x) for x in input().split()]
 
 tt = math.sqrt(2*(dtb+f)/ta)
 bt = f/bs
 
 if(bt < tt):
  print("Bolt")
 else:
  print("Tiger")

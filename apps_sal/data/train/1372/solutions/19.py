import math
try:
 t = int(input())
 
 while(t):
  l = [int(x) for x in input().split()]
  geta = math.sqrt( l[0]*l[0] + l[1]*l[1] )
  getb = math.sqrt( l[2]*l[2] + l[3]*l[3] )
  if(geta<getb):
   print("A IS CLOSER")
  else:
   print("B IS CLOSER")
  t -= 1

except:
 pass

import math
t = eval(input())
while(t > 0):
 h,s = input().split()
 h = int(h)
 s = int(s)
 if(((h*h*h*h) - (16*s*s)) < 0):
  print("-1")
 else:
  B = (math.sqrt((h*h) + math.sqrt((h*h*h*h) - (16*s*s))))/math.sqrt(2)
  P = (2*s)/B
  if(B > P):
   print('{0:.6f}'.format(P),'{0:.6f}'.format(B),'{0:.6f}'.format(h))
  else:
   print('{0:.6f}'.format(B),'{0:.6f}'.format(P),'{0:.6f}'.format(h))
 t = t-1

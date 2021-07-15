import math
t=eval(input())
while t>0:
 t-=1
 h,s = list(map(int,input().split()))
 try:
  bplush = math.sqrt(h*h+4*s)
  bminush = math.sqrt(h*h-4*s)
  base = (bplush + bminush)/2
  height =(bplush-bminush)/2
  a=[base,height,h]
  a.sort()
  for i in a:
   print(float(i), end=' ')
  print() 
 except:
  print("-1")

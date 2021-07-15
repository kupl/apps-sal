import math
t = int(input())
while(t!=0):
 n = int(input())
 c = 0
 while(n!=0):
  n = n - (int(math.sqrt(n))**2)
  c +=1
 t = t-1
 print(c)

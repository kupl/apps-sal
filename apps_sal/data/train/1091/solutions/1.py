# cook your dish here
import math
t = int(input())
for _ in range(t):
 n = int(input())
 count = 0
 for i in range(2, 2*n, 2):
  #print(i)
  h = math.sqrt(n*n-(i*i/4))
  #print(h)
  if h.is_integer()== True:
   count+=1
  else:
    count+=0
 if count>=1:
  print("YES")
 else:
  print("NO")

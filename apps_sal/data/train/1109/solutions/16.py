import math
for t in range(int(input())):
 n = int(input())
 i = 1
 count = 0
 x = math.sqrt(n)
 while (i<=x):
  if (n%i==0):
   count+=1
   if (i!=n/i):
    count+=1
  i+=1
 if (count%2==0):
  print("NO")
 else:
  print("YES")

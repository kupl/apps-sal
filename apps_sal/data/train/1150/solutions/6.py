import math
for _ in range(int(input())):
 count = 0
 n = int(input())
 while(n != 0):
  x = int(math.sqrt(n))
  count += 1
  n = n - x*x
 print(count)

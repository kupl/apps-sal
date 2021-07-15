import sys

for i in range(int(sys.stdin.readline().strip())):
 n, m = list(map(int, sys.stdin.readline().strip().split()))
 
 if n == 1:
  if m == 2:
   print("Yes")
  else:
   print("No")
 elif m == 1:
  if n == 2:
   print("Yes")
  else:
   print("No")
 else:
  if n * m & 1:
   print("No")
  else:
   print("Yes")

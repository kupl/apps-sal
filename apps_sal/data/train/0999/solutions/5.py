# cook your dish here
t = int(input())
for i in range(t):
 n = int(input())
 for i in range(1,n+1):
  print(" " * (n - i), end="")
  if i%2:
   for j in range(i): print(chr(ord('A')+j),end="")
  else:
   for j in range(i):print(j+1,end="")
  print()

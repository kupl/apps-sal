from sys import stdin

for _ in range(int(stdin.readline())):
 #n = int(stdin.readline())
 n, x = list(map(int, stdin.readline().split()))
 d, l = list(map(str, stdin.readline().split()))
 if d == 'R':
  x = n-x+1
 if l == 'H':
  if x % 2 == 0:
   print(x, 'E')
  else:
   print(x, 'H')
 else:
  if x % 2 == 0:
   print(x, 'H')
  else:
   print(x, 'E')
  


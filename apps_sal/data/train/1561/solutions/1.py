t = int(input())
for it in range(t):
 n = int(input())
 if n == 1:
  print(1, end=' ')
 elif n%2 == 0:
  for i in range(n//2, n//2+n):
   print(i, end=' ')
 else:
  for i in range(n//2, n//2+n):
   print(i, end=' ')
 print('')


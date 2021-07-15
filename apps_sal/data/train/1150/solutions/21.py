for i in range(int(input())):
 n = int(input())
 count = 0
 while n > 0:
  k = 1
  while k*k <= n:
   k += 1
  n -= (k-1)*(k-1)
  count += 1
 print(count)

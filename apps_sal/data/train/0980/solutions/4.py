def total_time(n, b, m):
 t = 0
 while n != 1:
  if n % 2 == 0:
   x = n / 2
  else:
   x = (n + 1) / 2
  t += (m * x)
  m *= 2
  t += b
  n -= x
 t += m
 return t


T = int(input())
for i in range(T):
 (N, B, M) = [int(z) for z in input().split()]
 print(total_time(N, B, M))


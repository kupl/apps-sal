def solve():
 n = int(input())
 a = bin(n)[2:]
 if a.count('0') == 0:
  if n == 1:
   print(2)
  else:
   print(n >> 1)
 else:
  print(-1)


def __starting_point():
 t = int(input())
 while t != 0:
  solve()
  t -= 1

__starting_point()

t = int(input())
while t != 0:
 n = int(input())
 k = int(input())
 i = k % n
 if i * 2 == n:
  print(n - 1)
 else:
  print(min(i, n - i) * 2)
 t -= 1

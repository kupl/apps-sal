for _ in range(int(input())):
 K = int(input())
 if K == 1:
  print(0)
 elif K == 2:
  print(0)
  print(*[1, 1])
 else:
  print(0)
  print(*[1, 1])
  l = 1
  c = 1
  for i in range(2, K):
   A = []
   for j in range(i+1):
    A.append(l+c)
    l = c
    c = A[-1]
   print(*A)

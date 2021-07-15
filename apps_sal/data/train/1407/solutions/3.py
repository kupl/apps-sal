t = int(input())

p2 = [1, 1, 2, 2]

p3 = [1, 2, 3]

p4 = [
 [1, 1, 2, 2],
 [3, 3, 4, 4],
 [2, 2, 1, 1],
 [4, 4, 3, 3],
]

for ti in range(t):
 n, m = map(int, input().split())

 if n == 1:
  print(2 if m > 2 else 1)
  for j in range(m):
   print(p2[j % 4], end=' ')
  print()

 elif m == 1:
  print(2 if n > 2 else 1)
  for i in range(n):
   print(p2[i % 4])

 elif n == 2:
  print(3 if m > 2 else 2)
  for j in range(m):
   print(p3[j % 3], end=' ')
  print()
  for j in range(m):
   print(p3[j % 3], end=' ')
  print()

 elif m == 2:
  print(3 if n > 2 else 2)
  for i in range(n):
   print(p3[i % 3], end=' ')
   print(p3[i % 3])

 else:
  print(4)
  for i in range(n):
   for j in range(m):
    print(p4[i % 4][j % 4], end=' ')
   print()


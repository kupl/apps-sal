lst=[1,2,3,4]
for _ in range(int(input())):
 m,n = map(int, input().split())
 ans = [[0 for i in range(m)] for i in range(n)]
 k = 0
 if n == 1:
  if m > 2:
   print(2)
  else:
   print(1)
  for i in range(m):
   print((i // 2) % 2 + 1)
 elif m == 1:
  if n > 2:
   print(2)
  else:
   print(1)
  for i in range(n):
   print((i // 2) % 2 + 1, end=" ")
 elif n == 2:
  if m > 2:
   print(3)
  else:
   print(2)
  for i in range(m):
   print(i % 3 + 1, i % 3 + 1)
 elif m == 2:
  if n > 2:
   print(3)
  else:
   print(2)
  for i in range(n):
   print(i % 3 + 1, end=" ")
  print()
  for i in range(n):
   print(i % 3 + 1, end=" ")
  
 else:
  print(4)
  lst = [[1,1,3,3],[2,2,4,4],[3,3,1,1,],[4,4,2,2]]
  for i in range(m) :
   for j in range(n) :
    print( lst[i%4][j%4] , end=" ")


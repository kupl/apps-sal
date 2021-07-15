def factorial(n):
 fact = 1
 for i in range(1, n+1):
  fact = fact * i
 return fact
t = int(input())
for _ in range(t):
 n, m = map(int, input().split())
 matrix = []
 for i in range(n):
  matrix.append(list(input()))
 collision = 0
 for i in range(m):
  count = 0
  for j in range(n):
   if matrix[j][i] == '1':
    count += 1
  # print('Count:', count)
  if count > 1:
   collision += ((count * (count-1)) // 2)
 print(collision)

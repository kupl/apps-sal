from math import sqrt

a, b = map(int, input().split())
pairs = 0

for i in range(1, a+1):
 for j in range(1, b+1):
  root = sqrt(i**2 + j)

  if not root - int(root):
   pairs += 1

print(pairs)

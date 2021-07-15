# Problem: http://www.codechef.com/JULY09/submit/CUBESUM/ 
# Author: Susam Pal

def computeA():
 X, Y, Z = [int(x) for x in input().split()]
 B = []
 for x in range(X):
  B.append([])
  for y in range(Y):
   B[-1].append([int(t) for t in input().split()])
   for z in range(Z):
    result = B[x][y][z]
    if x:
     result -= B[x - 1][y][z]
     if y:
      result += B[x - 1][y - 1][z]
      if z:
       result -= B[x - 1][y - 1][z - 1]
       
    if y:
     result -= B[x][y - 1][z]
     if z:
      result += B[x][y - 1][z - 1]
    if z:
     result -= B[x][y][z - 1]
     if x:
      result += B[x - 1][y][z - 1]
    print(result, end=' ')
   print()

test_cases = int(input())
for i in range(test_cases):
 computeA()


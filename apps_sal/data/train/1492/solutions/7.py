import sys

T = int(input())

result = ""

def getMin(matrix, N, M):
 smallest = sys.maxsize
 for i in range(0, N):
  for j in range(0, M):
   if matrix[i][j] < smallest:
    smallest = matrix[i][j]
 return smallest

for i in range(0, T):
 N = int(input())
 matrix = [[0 for x in range(2)] for x in range(N)]
 for j in range(0, N):
  text = input()
  for c in text:
   if(c == "a"):
    matrix[j][0] += 1
   else:
    matrix[j][1] += 1
 result += str(getMin(matrix, N, 2)) + "\n"

print(result)

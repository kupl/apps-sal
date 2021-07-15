for i in range(int(input())):
 n = int(input())
 arr = [[0]*n for j in range(n)]
 c = 1
 for j in range(n):
  for k in range(j+1):
   arr[k][j-k] = c
   c+=1
 for j in range(1,n):
  for k in range(n-j):
   arr[j+k][n-k-1] = c
   c+=1
 for j in arr:
  print(*j)

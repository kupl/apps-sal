from sys import stdin
t = int(stdin.readline())

def count(n, arr):
 loc = 0
 glob = 0
 for i in range(n-1):
  if arr[i] > arr[i+1]:
   loc += 1
 for i in range(n-1):
  for j in range(i+1, n):
   if glob > loc:
    return 0
   if arr[i] > arr[j]:
    glob += 1;
 if glob == loc:
  return 1
 return 0

for _ in range(t):
 n = int(stdin.readline())
 arr = list(map(int, stdin.readline().split()))
 result = count(n, arr)
 if result:
  print("YES")
 else:
  print("NO")

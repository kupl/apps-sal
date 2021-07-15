# cook your dish here
from collections import Counter
def solve(arr):
 n = len(arr)
 d = Counter(arr)
 if len(d.values()) != len(set(d.values())):
  return False
 i = 0
 j = 0 
 while i<n and j<n:
  j = i + 1 
  while j<n and arr[j] == arr[i]:
   j = j + 1 
  if j - i != d[arr[i]]:
   return False
  i = j 
 return True
 
for _ in range(int(input())):
 n = int(input())
 arr = [int(num) for num in input().split(' ')]
 ans = solve(arr)
 if ans == True:
  print('YES')
 else:
  print('NO')

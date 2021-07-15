from sys import stdin
from math import ceil, gcd

# Input data
#stdin = open("input", "r")


for _ in range(int(stdin.readline())):
 n = int(stdin.readline())
 arr = list(map(int, stdin.readline().split()))
 count_pos = 0
 ans = 0
 for i in range(n):
  if arr[i] >= 0:
   count_pos += 1
   ans += arr[i]

 case = []
 for i in range(count_pos):
  if arr[i] < 0:
   case.append(i + 1)
 for i in range(count_pos, n):
  if arr[i] >= 0:
   case.append(i + 1)
 print(ans)
 if len(case) == 0:
  print(0)
 else:
  print(len(case), end=' ')
  print(*case)


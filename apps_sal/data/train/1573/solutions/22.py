import math
from collections import deque, defaultdict
from sys import stdin, stdout
input = stdin.readline
# print = stdout.write
listin = lambda : list(map(int, input().split()))
mapin = lambda : list(map(int, input().split()))
for _ in range(int(input())):
 n = int(input())
 n1 = (n*(n-1))//2
 if n1%n:
  print("NO")
 else:
  print("YES")
  x = [0]
  for i in range(n1//n):
   x.append(1)
  for i in range(n1//n):
   x.append(0)
  for i in range(n):
   print("".join(map(str, x)))
   x = [x[-1]]+x[:-1]

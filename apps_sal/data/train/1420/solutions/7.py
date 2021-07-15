import math


def find_interleavings(a, b):
 c = list()

 def interleaf(i, j, l):
  if i == len(a) and j == len(b):
   c.append(l)
  elif i == len(a):
   interleaf(i, j + 1, l + [b[j]])
  elif j == len(b):
   interleaf(i + 1, j, l + [a[i]])
  else:
   interleaf(i + 1, j, l + [a[i]])
   interleaf(i, j + 1, l + [b[j]])

 interleaf(0, 0, [])
 return c


for _ in range(int(input())):
 n, m, k = list(map(int, input().split(" ")))
 a = list(map(int, input().split(" ")))
 b = list(map(int, input().split(" ")))
 res = 0

 ils = find_interleavings(a, b)
 #print(ils)
 for c in ils:
  num_blocks = 0
  prev = math.inf
  for i in c:
   if i != prev:
    num_blocks += 1
   prev = i
  # num_blocks += 1
  if num_blocks == k:
   res += 1
 print(res)


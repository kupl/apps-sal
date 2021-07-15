import sys

__author__ = 'm.melnik'

n, m, p = [int(i) for i in sys.stdin.readline().split()]
incs = {i: [] for i in range(1, n + 1)}

for i in range(p):
 x, y = [int(i) for i in sys.stdin.readline().split()]
 incs[x].append(y)

for i in range(1, n + 1):
 cur = 1
 cost = 0
 height = cur
 prev_height = 0
 # print(sorted(incs[i]))
 for j in sorted(incs[i]):
  if j == cur:
   height += 1
  elif j == cur + 1:
   if cur != 1:
    if height >= prev_height:
     cost += height - prev_height
    else:
     cost = -1
     break
   prev_height = height
   height = j + 1
   cur = j
  else:
   if cur != 1:
    if height >= prev_height:
     cost += height - prev_height
    else:
     cost = -1
     break
   if height > cur + 1:
    cost = -1
    break
   else:
    cost += j - height - 1
    cur = j
    height = j + 1
    prev_height = j - 1

 if cost != -1:
  if cur != m:
   if cur != 1:
    if height >= prev_height:
     cost += height - prev_height
    else:
     cost = -1
   if cost != -1:
    if height > cur + 1:
     cost = -1
    else:
     cost += m - height
  else:
   if cur != 1:
    if height >= prev_height:
     cost += height - prev_height
    else:
     cost = -1
 print(cost)


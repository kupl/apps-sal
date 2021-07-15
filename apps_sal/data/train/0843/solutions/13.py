def score(qn):
 
 import math
 maximum = math.inf
 score = 0
 for i in reversed(list(range(0, len(qn)))):
  
  temp = -1
  for j in qn[i]:
   
   if j > temp and j < maximum:
    temp = j
  if temp == -1:
   return -1
  else:
   score += temp
   maximum = temp
 return score


import sys
c = 0
for line in sys.stdin:
 if c == 0:
  t = int(line.strip())
  c = 2
 else:
  if c%2 == 0:
   new = line.split()
   N = int(new[0].strip())
   qn = []
   c = 5
   count = 1
  elif c ==5:
   a = list(map(int, line.split()))
   
   qn.append(a)
   count += 1
   if count == N+1:
    c = 2
    print(score(qn))


# cook your dish here
from collections import defaultdict as dd
for _ in range(int(input())) :
 cont = dd(list)
 n, c = list(map(int,input().split()))
 for i in range(n):
  x, y = list(map(int,input().split()))
  cont[ ( x-y , ((x%c) + c )%c ) ].append((x,y))
  #cont[ (x-y,(x%c) ) ].append((x,y))
 checkpoints = len(cont)
 moves = 0
 for i in cont:
  v = cont[i]
  v.sort()
  pivot = v[ len(v)//2 ]
  for j in v:
   moves += abs(pivot[0] - j[0])//c
 print(checkpoints,moves)


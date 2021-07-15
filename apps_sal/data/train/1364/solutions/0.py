t = int(input())

for i in range(t):
 n, c = list(map(int,input().split()))

 pts = {}
 moves = 0

 for i in range(n):
  x, y = list(map(int,input().split()))
  if (y-x,x%c) in pts:
   pts[(y-x,x%c)].append(x)
  else:
   pts[(y-x,x%c)] = [x]
 
 for i in pts:
  arc = sorted(pts[i])
  
  for j in arc:
   moves = moves + abs((j-arc[len(arc)//2]))//c
 
 print(len(pts),moves)


   




for t in range(int(input())):
 n,c = map(int,input().split())
 d = {}
 for i in range(n):
  x,y = map(int,input().split())
  t = x-y
  if t not in d:
   d[t] = [[x,y]]
  else:
   d[t].append([x,y])
 checkpoints = 0
 moves=0
 for i in d:
  points = d[i]
  mod={}
  for j in range(len(points)):
   t = points[j][0]%c
   if t not in mod:
    mod[t]=[points[j]]
   else:
    mod[t].append(points[j])
  for j in mod:
   checkpoints+=1
   check = mod[j]
   check = sorted(check, key = lambda x:x[0])
   mid = check[len(check)//2][0]
   for k in range(len(check)):
    moves+= (abs(mid-check[k][0])//c)
 print(checkpoints,moves)

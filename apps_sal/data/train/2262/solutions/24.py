import sys
input = sys.stdin.readline
r,c,n = map(int,input().split())
xy = [list(map(int,input().split())) for i in range(n)]
ls = []
for x1,y1,x2,y2 in xy:
  if (x1 in (0,r) or y1 in (0,c)) and (x2 in (0,r) or y2 in (0,c)):
    k = []
    for x,y in ((x1,y1),(x2,y2)):
      if x == 0:
        s = 2*r+2*c-y
      if x == r:
        s = r+y
      if y == 0:
        s = x
      if y == c:
        s = 2*r+c-x
      k.append(s)
    t = len(ls)//2+1
    ls.append((k[0],t))
    ls.append((k[1],t))
if not ls:
  print("YES")
  return
ls.sort()
lsi = list(map(list,zip(*ls)))[1]
m = len(lsi)
stack = []
for i in lsi:
  if not stack:
    stack.append(i)
  else:
    if stack[-1] == i:
      stack.pop()
    else:
      stack.append(i)
if stack:
  print("NO")
else:
  print("YES")

import sys,math

t = int(sys.stdin.readline())
ds = [(0,1),(1,0),(0,-1),(-1,0)]
for _ in range(t):
 x, y, d = 0, 0, 0
 path = sys.stdin.readline().split()
 for ins in path:
  if ins == 'L':
   d = (d-1)&3
  elif ins == 'R':
   d = (d+1)&3
  else:
   x,y = x+ds[d][0]*int(ins), y+ds[d][1]*int(ins)
 dist = math.sqrt(float(x**2 + y**2))
 if y > 0:
  if x > 0:
   dir = 'NE'
  elif x < 0:
   dir = 'NW'
  else:
   dir = 'N'
 elif y < 0:
  if x > 0:
   dir = 'SE'
  elif x < 0:
   dir = 'SW'
  else:
   dir = 'S'
 else:
  if x > 0:
   dir = 'E'
  elif x < 0:
   dir = 'W'
  else:
   dir = ''
 print('%.1f%s' % (math.floor(dist*10)/10.0,dir))


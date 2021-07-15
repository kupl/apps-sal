from collections import Counter
try:
 for _ in range(int(input())):
  n=int(input())
  s=input()
  d1=dict(Counter(s))
  
  u,d,r,l=0,0,0,0
  if 'U' in d1:
   u=d1['U']
  else:
   u=0
  if 'D' in d1:
   d=d1['D']
  else:
   d=0
  if 'R' in d1:
   r=d1['R']
  else:
   r=0
  if 'L' in d1:
   l=d1['L']
  else:
   l=0
  x=0
  y=0
  if l==r:
   x=0
  elif l>r:
   x=-(l-r)
  elif r>l:
   x=r-l
  if u==d:
   y=0
  elif d>u:
   y=-(d-u)
  elif u>d:
   y=u-d
  #  print(x,y)
  if x==0 and y==0:
   print(n)
   continue
  
  print(n-(abs(x)+abs(y)))
except:
 pass


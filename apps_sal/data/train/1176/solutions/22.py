import math

g = {
 1 : (1,2),
 2 : (3,2),
 3 : (4,2),
 4 : (5,2),
 5 : (1,2)
}

t = int(input().strip())

for tt in range(t):

 str = input().strip()
 v = 1

 for j in range(len(str)):
  if str[j] == '0':
   v = g[v][0]
  else:
   v = g[v][1]

 if v==5:
  print('YES')
 else:
  print('NO')

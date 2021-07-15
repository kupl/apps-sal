try:
 from sys import stdin as si , stdout as so

 for _ in range(int(si.readline())):
  m = {}
  n = int(si.readline())
 
  for i in range(n):
   a , b = map(int , si.readline().split())
   if a not in m:
    m[a] = b
   else:
    m[a] = max(m[a] , b)
 
  if len(m) < 3:
   so.write(str(0) + '\n')
  else:
   l = list(m.values())
   l.sort()
   so.write(str(l[-1] + l[-2] + l[-3]) + '\n')
except:
 pass

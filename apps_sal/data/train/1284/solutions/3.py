for _ in range(int(input())):
 n = int(input())
 l = list(map(int,input().split()))
 l.sort()
 a = n//4
 m = []
 for i in l:
  m.append(l.count(i))
 if max(m)>a:
  print(-1)
 
 else:
  x = a
  y = x+a
  z = y+a
  if l[x]==l[x-1]:
   print(-1)
  elif l[y]==l[y-1]:
   print(-1)
  elif l[z]==l[z-1]:
   print(-1)
  else:
   print(l[x],l[y],l[z])


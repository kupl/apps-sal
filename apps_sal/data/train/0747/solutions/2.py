# cook your dish here
from collections import Counter
t = int(input())
for _ in range(t):
 n = int(input())
 arr = list(map(int, input().split()))
 arr.sort()
 g = Counter(arr)
 s = list(g.values())
 seti = list(set(arr))
 seti = sorted(seti)
 if len(seti)==n:
  print("YES")
  print(*arr)
 else:
  h = [item for item,count in list(g.items()) if count>=3]
  if h:
   print("NO")
  elif g[arr[-1]]==2:
   print("NO")
  else:
   k = [item for item,count in list(g.items()) if count==2]
   k = sorted(k, reverse = True)
   seti.extend(k)
   print("YES")
   print(*seti)


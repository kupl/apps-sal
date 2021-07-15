# cook your dish here
from difflib import get_close_matches
for _ in range(int(input())):
 n, q = map(int, input().split())
 mydic = {}
 vis = {}
 for i in range(n):
  temp = input()
  mydic[temp] = 1
 for i in range(q):
  temp = input()
  if temp in mydic.keys():
   print(temp)
  else:
   x = get_close_matches(temp, mydic.keys(), cutoff = 0.7)
   if len(x) > 0:
    mydic.pop(x[0])
    vis[x[0]] = 1
    print(x[0])
   else:
    print(get_close_matches(temp, vis.keys(), cutoff = 0.7)[0])

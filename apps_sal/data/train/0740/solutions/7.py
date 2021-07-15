from sys import stdin as si

def __starting_point():
 for _ in range(int(si.readline().strip())):
  _, _, k = list(map(int, si.readline().strip().split()))
  lookup = {}
  for i in range(k):
   x, y = list(map(int, si.readline().strip().split()))
   def check(d):
    if d in lookup:
     del lookup[d]
    else:
     lookup[d] = True
   check((x-1, y-1, x-1, y))
   check((x-1, y-1, x, y-1))
   check((x-1, y, x, y))
   check((x, y-1, x, y))
  print(len(lookup))

__starting_point()

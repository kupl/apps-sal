import math
import sys

def _int():
 return int(sys.stdin.readline())

def _ints():
 return list(map(int, sys.stdin.readline().split()))

def _intarr():
 return list(map(int, sys.stdin.readline().split()))

def _str():
 return sys.stdin.readline()

def _strarr():
 return sys.stdin.readline().split()

def adj(a, b, c):
 if b != opp[a] and b != opp[c] and a != opp[c]:
  return True
 return False

t = _int()

opp = [1, 0, 3, 2, 5, 4]

for _ in range(t):
 c = _strarr()
 cd = dict()
 for i in range(len(opp)):
  ind = cd.get(c[i], [])
  ind.append(i)
  cd[c[i]] = ind
 
 #print(cd)

 found = False
 for k in list(cd.keys()):
  ind = cd.get(k, [])
  if len(ind) == 3:
   if adj(ind[0], ind[1], ind[2]):
     found = True
  elif len(ind) == 4:
   if adj(ind[0], ind[1], ind[2]):
    found = True
   elif adj(ind[0], ind[1], ind[3]):
    found = True
   elif adj(ind[0], ind[2], ind[3]):
    found = True
   elif adj(ind[1], ind[2], ind[3]):
    found = True
  elif len(ind) >= 5:
   found = True
  if found:
   break
 print("YES" if found else "NO")


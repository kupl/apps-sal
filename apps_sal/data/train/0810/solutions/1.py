# cook your dish here
from bisect import bisect_left 
 
def BinarySearch(a, x): 
 i = bisect_left(a, x) 
 if i != len(a) and a[i] == x: 
  return i 
 else: 
  return -1

for _t in range(int(input())):
 _n, q = list(map(int, input().split()))
 mounts = list(map(int, input().split()))
 for _q in range(q):
  query = list(map(int, input().split()))
  if query[0] == 0:
   mounts[query[1]] = query[2]
  else:
   curr = query[1]
   prev = sorted(mounts[:curr+1])
   for m in mounts[curr+1:]:
    if m > mounts[curr] and BinarySearch(prev, m) == -1:
     print(m)
     break
   else:
    print(-1)
     


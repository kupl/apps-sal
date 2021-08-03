from collections import deque
 
 class Solution:
     def slidingPuzzle(self, b):
         seen = set()
         q = deque()
         q.append(([1,2,3,4,5,0], 5, 0))
         while q:
             u, p, m = q.popleft()
             if u == b[0] + b[1]:
                 return m
             for np in [p-1 if p != 3 else -1, p+1 if p != 2 else -1, p-3, p+3]:
                 if 0 <= np < 6:
                     v = u[:]
                     v[p], v[np] = v[np], v[p]
                     if tuple(v) not in seen:
                         seen.add(tuple(v))
                         q.append((v[:], np, m+1))
         return -1

t=int(input())

for _ in range(t):
 R, G, B, M = [int(x) for x in input().split(' ')]
 r = [int(x) for x in input().split(' ')]
 g = [int(x) for x in input().split(' ')]
 b = [int(x) for x in input().split(' ')]
 r.sort(reverse=True)
 g.sort(reverse=True)
 b.sort(reverse=True)
 
 for y in range(M):
  m = max(r[0], g[0], b[0])
  if m == r[0]:
   r = [x//2 for x in r]
  elif m == g[0]:
   g = [x//2 for x in g]
  elif m == b[0]:
   b = [x//2 for x in b]
 
 print(max(r[0], g[0], b[0]))
 


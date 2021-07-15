t = int(input())
for _ in range(t):
 n = int(input())
 x, p = [], []
 for __ in range(n):
  line = list(map(int, input().split()))
  x.append(line[0])
  p.append(line[1])
 g = []
 for i in range(n-1):
  g.append(x[i+1] - x[i])
 bois = []
 bois.append(g[0])
 for k in range(n-2):
  bois.append(g[k+1] + g[k])
 bois.append(g[n-2])
 bois.sort()
 p.sort()
 ans = 0
 for i in range(n):
  ans += p[i] * bois[i]
 print(ans)
 
  


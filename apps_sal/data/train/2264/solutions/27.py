from heapq import heapify, heappush, heappop
def conv(c, p, pp):
  return (c*N + p)*N + pp
def rev(X):
  pp = X % N
  X //= N
  p = X % N
  c = X // N
  return (c, p, pp)

MOD = 10**9 + 7
N, M = list(map(int,input().split()))
s, t = list(map(int,input().split()))
s -= 1; t -= 1;
I = [[] for _ in range(N)]
edges = []
for _ in range(M):
  u, v, c = list(map(int,input().split()))
  u -= 1; v -= 1;
  I[u].append((v, c))
  I[v].append((u, c))
  edges.append(conv(c,u,v))
  
fin_i = [0 for _ in range(N)]
ml_i = [0 for _ in range(N)]
fin_r = [0 for _ in range(N)]
ml_r = [0 for _ in range(N)]

  
def dijkstra(s, fin, ml):
  task = [conv(0, s, s)]
  fin[s] = 1
  ml[s] = 0
  vis = set()
  while task:
    while True:
      if not task:
        return
      #print(task)
      c, p, pp = rev(heappop(task))
      #print(c, p, pp, task)
      if p in vis and c == ml[p]:
        #print(p, pp, 1, vis)
        fin[p] += fin[pp]
        fin[p] %= MOD
      elif p not in vis:
        #print(p)
        break
    if p != s:
      #print(p, pp, 2)
      fin[p] += fin[pp]
      fin[p] %= MOD
      ml[p] = c
    vis.add(p)
    #print(p, I[p])
    for q, c_n in I[p]:
      if q not in vis:
        heappush(task, conv(c+c_n, q, p))
  return

dijkstra(s, fin_i, ml_i)
dijkstra(t, fin_r, ml_r)
#print(ml_i)
#print(fin_i)
#print(ml_r)
#print(fin_r)
L = ml_i[t]

ans = 0
for X in edges:
  c, u, v = rev(X)
  if ml_i[u] + c + ml_r[v] == L and ml_i[u]*2 < L < ml_i[v]*2:
    #print(u, v, fin_i[u], fin_r[v])
    ans += (fin_i[u] * fin_r[v]) ** 2
  u, v = v, u
  if ml_i[u] + c + ml_r[v] == L and ml_i[u]*2 < L < ml_i[v]*2:
    #print(u, v, fin_i[u], fin_r[v])
    ans += (fin_i[u] * fin_r[v]) ** 2
    ans %= MOD
for p in range(N):
  if 2*ml_i[p] == L:
    #print(p, fin_i[p] * fin_r[p])
    ans += (fin_i[p] * fin_r[p]) ** 2
    ans %= MOD
    
print(((fin_i[t]**2 - ans) %MOD))


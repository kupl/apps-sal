t = int(input())
while(t):
 t -= 1
 n, m, k = list(map(int, input().split()))
 g = []
 for i in range(1000001):
  g.append([])
 while(m):
  m -= 1
  x, y = list(map(int, input().split()))
  g[x].append(y)
  g[y].append(x)
 a = [0] + list(map(int, input().split()))
 ans = []
 vis = [0]*1000001
 for i in range(1, n+1):
  if(vis[i] == 0):
   vis[i] = 1
   val = a[i]
   bfsQ = [i]
   while(bfsQ):
    x = bfsQ[0]
    del bfsQ[0]
    for y in g[x]:
     if(vis[y] == 0):
      val += a[y]
      vis[y] = 1
      bfsQ.append(y)
   ans.append(val)
 ans = sorted(ans)
 if(k>len(ans)):
  print(-1)
 else:
  print(sum(ans[:k//2]) + sum(ans[len(ans)-(k-k//2):]))

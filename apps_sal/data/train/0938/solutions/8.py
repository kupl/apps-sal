for t in range(int(input())):
 n = int(input())
 a = list(map(int, input().split()))
 d = {}
 for i in range(n):
  d[a[i]] = []
 for i in range(n):
  d[a[i]].append(i) 
 ans = 0
 for i in range(n):
  temp = []
  pos = []
  visited = {}
  for j in range(i,n):
   if (visited.get(a[j], True)):
    visited[a[j]] = False
    temp.append(a[j])
    pos += d[a[j]]
    pos.sort()
    if (pos[-1] != (n-1)):
     f = pos + [n]
    else:
     f = pos
   curr = 0
   for p in range(1,len(f)):
    if (f[p] > j):
     curr += (f[p] - f[p-1] - 1) * (f[p] - f[p-1]) / 2
   ans += curr
 print(ans)


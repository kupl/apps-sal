def dfs(i):
 visited[i]=True
 musuemsPossible=musuems[i]
 for j in neighbours[i]:
  if(not visited[j]):
   musuemsPossible+=dfs(j)
 return musuemsPossible

t = int(input())
for _ in range(t):
 n,m,k = list(map(int, input().split())) 
 neighbours=[]
 visited=[]
 for i in range(n):
  visited.append(False)
  neighbours.append([])
 for _ in range(m):
  a,b = list(map(int, input().split()))
  neighbours[a-1].append(b-1)
  neighbours[b-1].append(a-1)
 
 musuems=[int(x) for x in input().split()]

 mususeumsBigNode=[]
 for i in range(n):
  if(not visited[i]):
   mususeumsBigNode.append(dfs(i))
 
 if len(mususeumsBigNode) < k:print(-1)
 else:
  mususeumsBigNode.sort()
  if k % 2 == 0:
   k //= 2
   ans = sum(mususeumsBigNode[:k]+mususeumsBigNode[-k:])
  else:
   k //= 2
   ans = mususeumsBigNode[-k-1]
   if k > 0:ans += sum(mususeumsBigNode[:k]+mususeumsBigNode[-k:])
  print(ans)


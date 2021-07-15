def dfs(node):
 nonlocal adj,leaf
 val=0
 flag=0
 for i in adj[node]:
  x= dfs(i)
  val+=x
  if x==0:
   flag=1
 leaf+=val-val%3
 if val%3==0 and flag==0:
  return 1
 else:
  return 0
for _ in range(int(input())):
 n=int(input())
 adj=[[] for i in range(n+2)]
 arr=[int(i) for i in input().split()]
 leaf=0
 #print(adj)
 for i in range(2,n+1):
  #print(i,arr[i-2])
  adj[arr[i-2]].append(i)
  
 dfs(1)
 print(n-leaf)

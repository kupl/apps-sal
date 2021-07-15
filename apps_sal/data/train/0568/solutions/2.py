
test=int(input())
for t in range(test):
 n= int(input())

 adj=[[] for i in range(n+1)]

 for _ in range(n-1):
  a,b=list(map(int,input().split()))
  adj[a].append(b)
  adj[b].append(a)
 

 #print(adj)
 root=1
 q,s=[root],set([root])

 for x in q:
  adj[x]= [p for p in adj[x] if p not in s]
  q.extend(adj[x])
  s.update(adj[x])

 #print(adj)
 ans=True
 for i in range(n+1):
  if(len(adj[i]) %3!=0):
   ans=False
 if(ans):
  print("YES")
  for i in range(n+1):
   while(len(adj[i])):
    print(i,adj[i][0],adj[i][1],adj[i][2])
    adj[i].pop(0)
    adj[i].pop(0)
    adj[i].pop(0)
 else:
  print("NO")


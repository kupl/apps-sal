sx,sy,tx,ty=map(int,input().split())
n=int(input())
l=[list(map(int,input().split())) for i in range(n)]
l.append([sx,sy,0])
l.append([tx,ty,0])

def dijkstra(s,n,cost):
  d=[float("inf")]*n
  used=[False]*n
  d[s]=0
  while True:
    v=-1
    for i in range(n):
      if (not used[i]) and (v==-1):
        v=i
      elif (not used[i]) and d[i]<d[v]:
        v=i
    if v==-1:
      break
    used[v]=True
    for j in range(n):
      d[j]=min(d[j],d[v]+cost[v][j])
  return d

cost=[[float("inf") for i in range(n+2)] for i in range(n+2)] 
for i in range(n+2):
  for j in range(n+2):
    cost[i][j]=max(((l[i][0]-l[j][0])**2+(l[i][1]-l[j][1])**2)**0.5-l[i][2]-l[j][2],0)
    cost[j][i]=max(((l[i][0]-l[j][0])**2+(l[i][1]-l[j][1])**2)**0.5-l[i][2]-l[j][2],0)
print(dijkstra(n,n+2,cost)[n+1])

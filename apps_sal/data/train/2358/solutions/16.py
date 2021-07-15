a,b,c,d=map(int, input().split())
N=int(input())
def dijkstra(s,n,w,cost):
    #始点sから各頂点への最短距離
    #n:頂点数,　w:辺の数, cost[u][v] : 辺uvのコスト(存在しないときはinf)
    d = [float("inf")] * n
    used = [False] * n
    d[s] = 0
    
    while True:
        v = -1
        #まだ使われてない頂点の中から最小の距離のものを探す
        for i in range(n):
            if (not used[i]) and (v == -1):
               v = i
            elif (not used[i]) and d[i] < d[v]:
                v = i
        if v == -1:
               break
        used[v] = True
               
        for j in range(n):
               d[j] = min(d[j],d[v]+cost[v][j])
    return d
R=[0]*(N+2)
A=[]
for i in range(N):
  x,y,r=map(int, input().split())
  A.append((x,y))
  R[i]=r
A.append((a,b))
A.append((c,d))
cost=[[float('inf') for i in range(N+2)] for i in range(N+2)]
for i in range(N+1):
  for j in range(i+1,N+2):
    d=(A[i][0]-A[j][0])**2+(A[i][1]-A[j][1])**2
    cost[i][j]=max(0,d**0.5-(R[i]+R[j]))
    cost[j][i]=max(0,d**0.5-(R[i]+R[j]))
D=dijkstra(N,N+2,(N+2)*(N+1)//2,cost)
print(D[N+1])

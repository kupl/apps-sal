XS,YS,XT,YT=map(int,input().split())
N=int(input())
V=[[XS,YS,0],[XT,YT,0]]
for i in range(N):
  V.append(list(map(int,input().split())))
INF=10**12
G=[[INF]*len(V) for i in range(len(V))]
def d(a,b):
  return ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5
for i in range(len(V)):
  G[i][i]=0
  for j in range(len(V)):
    G[i][j]=max(0,d(V[i][:2],V[j][:2])-V[i][2]-V[j][2])
D=[0]*len(V)
U=[0]*len(V)
def ijk(s):
  nonlocal D,U,G,V,INF
  for i in range(len(V)):
    D[i]=INF
    U[i]=False
  D[s]=0
  v=0
  while True:
    v=-1
    for i in range(len(V)):
      if not(U[i]) and (v==-1 or D[i]<D[v]):
        v=i
    if v==-1:
      break
    U[v]=True
    for i in range(len(V)):
      D[i]=min(D[i],D[v]+G[v][i])

ijk(0)
print(D[1])

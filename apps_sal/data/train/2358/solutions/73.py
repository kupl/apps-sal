import heapq
INFTY = 10**10
def f(x,y):
    return ((x[0]-y[0])**2+(x[1]-y[1])**2)**0.5
xs,ys,xt,yt = map(int,input().split())
N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]
A.insert(0,[xs,ys,0])
A.append([xt,yt,0])
dist = [INFTY for _ in range(N+2)]
hist = [0 for _ in range(N+2)]
heap = [(0,0)]
dist[0]=0
hist[0]=1
while heap:
    d,x = heapq.heappop(heap)
    if dist[x]<d:continue
    hist[x]=1
    for i in range(N+2):
        if hist[i]==0:
            if dist[i]>d+max(f(A[x][:2],A[i][:2])-(A[x][2]+A[i][2]),0):
                dist[i]=d+max(f(A[x][:2],A[i][:2])-(A[x][2]+A[i][2]),0)
                heapq.heappush(heap,(dist[i],i))
print(dist[N+1])

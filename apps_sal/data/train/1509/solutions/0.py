#for _ in range(int(input()):
#n,m = map(int,input().split())
#x = [int(w) for w in input().split()]
#n = int(input())
#x = [int(input()) for _ in range(n)]
#for i in range(n):
#dt = {} for i in x:dt[i] = dt.get(i,0)+1
#dt = {k:v for k,v in sorted(x.items(), key=lambda i: i[1])}

m,n = map(int,input().split())  # top,right,bottom,left
x = []
for i in range(m):
    x.append([])
    for j in range(n):
        clr = [w for w in input().split()]
        x[i].append(clr)

import queue as Q                
dp = [float('inf')]*m
for i in range(m):
    dp[i] = [float('inf')]*n
dp[m-1][n-1] = 0
pq = Q.PriorityQueue()
pq.put([dp[m-1][n-1],m-1,n-1])
visited = set()
xx,yy = [-1,0,1,0],[0,1,0,-1] # top,right,bottom,left
while not pq.empty():
    pop = pq.get()
    cx,cy = pop[1],pop[2]
    if (cx,cy) not in visited:
        visited.add((cx,cy))
        for k in range(4):
            nx,ny = cx+xx[k],cy+yy[k]
            if 0<=nx<m and 0<=ny<n and (nx,ny) not in visited:
                clr = x[cx][cy][k]
                #print("*",nx,ny,"_",k,clr)
                ind = x[nx][ny].index(clr)
                cost = (k-(ind+2)%4)%4
                #print(cost)
                if dp[cx][cy]+cost < dp[nx][ny]:
                    dp[nx][ny] = dp[cx][cy]+cost
                    pq.put([dp[nx][ny],nx,ny])
        #print("#############")
#print(dp)
print(dp[0][0])

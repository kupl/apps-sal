N,M=list(map(int,input().split()))
edge=[set([]) for i in range(N)]
for i in range(M):
    a,b=list(map(int,input().split()))
    edge[a-1].add(b-1)
    edge[b-1].add(a-1)

cedge=[[] for i in range(N)]
for i in range(N):
    for j in range(N):
        if j not in edge[i] and j!=i:
            cedge[i].append(j)

ans=[]
def is_bipartgraph():
    color=[0]*N
    used=[False]*N
    for i in range(N):
        if not used[i]:
            stack=[(i,1)]
            black=0
            white=0
            while stack:
                v,c=stack.pop()
                color[v]=c
                black+=(not used[v])*(c==1)
                white+=(not used[v])*(c==-1)
                used[v]=True
                for nv in cedge[v]:
                    if color[nv]==color[v]:
                        return False
                    elif color[nv]==0:
                        stack.append((nv,-c))
            ans.append([black,white])
    return True

if is_bipartgraph():
    dp=[[False for i in range(0,N+1)] for j in range(len(ans))]
    a,b=ans[0]
    dp[0][a],dp[0][b]=True,True
    for i in range(1,len(ans)):
        a,b=ans[i]
        for j in range(0,N+1):
            test=False
            if j>=a:
                test=test|dp[i-1][j-a]
            if j>=b:
                test=test|dp[i-1][j-b]
            dp[i][j]=test
    ans=0
    for i in range(0,N+1):
        if dp[-1][i] and abs(ans-N/2)>abs(i-N/2):
            ans=i
    ans2=N-ans
    print((ans*(ans-1)//2+ans2*(ans2-1)//2))
else:
    print((-1))


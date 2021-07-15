import sys
from collections import deque

input=sys.stdin.readline
#sys.setrecursionlimit(2*10**5)

for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    data=[[] for i in range(n)]
    for i in range(n):
        data[a[i]-1].append(i)
        data[b[i]-1].append(i)
    for i in range(n):
        if len(data[i])!=2:
            print(-1)
            break
    else:
        edge=[[] for i in range(n)]
        for i in range(n):
            u,v=data[i][0],data[i][1]
            edge[u].append((v,i))
            edge[v].append((u,i))

        seen=[False]*n
        temp=[]
        res=0
        def dfs(v,cond):
            nonlocal temp,res
            res.append(v)
            if cond==1:
                up,down=a[v],b[v]
            else:
                up,down=b[v],a[v]

            for nv,val in edge[v]:
                if not seen[nv]:
                    seen[nv]=True
                    if a[nv]==up or b[nv]==down:
                        temp.append(nv)
                        dfs(nv,-1)
                    else:
                        dfs(nv,1)

        def bfs(i):
            nonlocal temp,res
            deq=deque([(i,1)])
            while deq:
                v,cond=deq.popleft()
                res.append(v)
                if cond==1:
                    up,down=a[v],b[v]
                else:
                    up,down=b[v],a[v]

                for nv,val in edge[v]:
                    if not seen[nv]:
                        seen[nv]=True
                        if a[nv]==up or b[nv]==down:
                            temp.append(nv)
                            deq.append((nv,-1))
                        else:
                            deq.append((nv,1))

        ans=[]
        for i in range(0,n):
            if not seen[i]:
                res=[]
                temp=[]
                seen[i]=True
                bfs(i)
                if len(res)-len(temp)>=len(temp):
                    ans+=temp
                else:
                    temp=set(temp)
                    for v in res:
                        if v not in temp:
                            ans.append(v)
        if ans:
            ans=[ans[i]+1 for i in range(len(ans))]
        print(len(ans))
        print(*ans)


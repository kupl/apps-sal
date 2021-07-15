from collections import deque
for _ in range(int(input())):
    n=int(input())
    s=list(input())
    dist=[float('inf') for i in range(n)]
    adj=[[] for i in range(n)]
    q=deque()
    vis=[False]*n
    for i in range(n):
        if i!=0:
            adj[i].append(i-1)
        if i!=n-1:
            adj[i].append(i+1)
        if s[i]=="1":
            dist[i]=0
            q.append(i)
            # vis[i]=True
    d=int(input())
    p=[int(o) for o in input().split()]
    while q:
        s=q.popleft()
        vis[s]=True
        if dist[s]<d:
            kk=p[dist[s]]
            if kk-2 in adj[kk-1]:
                adj[kk-1].remove(kk-2)
            if kk-2 >0:
                if kk-1 in adj[kk-2]:
                    adj[kk-2].remove(kk-1)
        for i in adj[s]:
            if not vis[i]:
                q.append(i)
                dist[i]=min(dist[s]+1,dist[i])
    ans=0
    for i in dist:
        if i<=d:
            ans+=1
    print(ans)



        



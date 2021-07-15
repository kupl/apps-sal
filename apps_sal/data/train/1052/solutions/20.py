def dsum(n):
    return sum(int(i) for i in str(n))
for _ in range(int(input())):
    n,d=map(int,input().split())
    q=[n]
    lev=0 
    res=[]
    vis={}
    dist={}
    dist[n]=0
    lev=0 
    res.append([n,0])
    while q:
        siz=len(q)
        lev+=1 
        for i in range(siz):
            t=q.pop(0)
            if t+d not in vis:
                vis[t+d]=1 
                res.append([t+d,lev])
                #print(t,t+d,lev)
                dist[t+d]=dist.get(t)+1
                q.append(t+d)
            if dsum(t) not in vis:
                vis[dsum(t)]=1 
                res.append([dsum(t),lev])
                #print(t,dsum(t),lev)
                dist[dsum(t)]=dist.get(t)+1 
                q.append(dsum(t))
                
        if lev==32:
            break 
    #print(res)
    res.sort(key=lambda x:x[0])
    #print(res)
    print(res[0][0],res[0][1])

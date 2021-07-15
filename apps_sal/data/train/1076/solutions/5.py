def bfs(tr,sp,d):
    temp=[sp]
    vl=[-1]*len(tr)
    vl[sp]=0
    while(len(temp)>0):
        z=temp.pop(0)
        if(vl[z]>=d):
            continue
        for e in tr[z]:
            if(vl[e]==-1):
                vl[e]=vl[z]+1
                temp.append(e)
    return [i for i in range(len(vl)) if vl[i]==d]

def myfunc():
    n,q=list(map(int,input().split()))
    tr=[[] for _ in range(n+1)]
    for _ in range(n-1):
        u,v=list(map(int,input().split()))
        tr[u].append(v)
        tr[v].append(u)
    for qn in range(q):
        a,da,b,db=list(map(int,input().split()))
        ta=set(bfs(tr,a,da))
        tb=set(bfs(tr,b,db))
        x=list(ta.intersection(tb))
        if(len(x)>0):
            print(x[0])
        else:print(-1)


t=int(input())
for _ in range(t):
    myfunc()

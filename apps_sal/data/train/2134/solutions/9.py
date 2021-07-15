from collections import deque,defaultdict
n=int(input())
g=defaultdict(list)
a=list(map(int,input().split()))
for i in range(n-1):
    g[a[i]].append(i+2)
    g[i+2].append(a[i])
s=list(map(int,input().split()))
visited=[False]*(n+1)
q=deque();q.append(1);visited[1]=True
val=[0]*(n+1);val[1]=s[0]
#print(val)
while len(q)>0:
    v=q.popleft()
    b=[]
    for i in g[v]:
        if not visited[i]:
            if s[v-1]==-1:
                b.append(s[i-1])
            else:
                if v>1:
                    val[v]=s[v-1]-s[g[v][0]-1]
            q.append(i)
            visited[i]=True
    if b!=[] and not all([x>=s[g[v][0]-1] for x in b]):
        print(-1)
        return
    elif b!=[]:
        val[v]=min(b)-s[g[v][0]-1]
        s[v-1]=val[v]+s[g[v][0]-1]
    else:
        if s[v-1]!=-1 and v>1:
            val[v]=s[v-1]-s[g[v][0]-1]
    


print(sum(val))


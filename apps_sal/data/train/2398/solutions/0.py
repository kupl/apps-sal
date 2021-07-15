import sys

sys.setrecursionlimit(10 ** 5)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def maketo():
    atoi=[[] for _ in range(n)]
    for i,a in enumerate(aa):
        if a<1 or a>n:return True
        atoi[a-1].append(i)
        if len(atoi[a-1])>2:return True
    for a in range(n):
        u,v=atoi[a]
        if u+n==v:continue
        to[u].append((v+n)%(n*2))
        to[v].append((u+n)%(n*2))
    return False

def dfs(u):
    flap[u%n]=(u>=n)*1
    cur[u>=n].append(u%n+1)
    stack=[u]
    while stack:
        u=stack.pop()
        for v in to[u]:
            if flap[v%n]==-1:
                flap[v % n]=(v>=n)*1
                cur[v >= n].append(v % n+1)
                stack.append(v)
            elif flap[v % n]!=(v>=n)*1:return True
    return False

for _ in range(II()):
    n=II()
    aa=LI()+LI()
    to=[[] for _ in range(n*2)]

    if maketo():
        print(-1)
        continue
    #print(to)

    ans = []
    flap=[-1]*n
    ng=False
    for u in range(n):
        #u+=n
        if flap[u%n]!=-1:continue
        cur=[[],[]]
        ng=dfs(u)
        if len(cur[0])<len(cur[1]):ans+=cur[0]
        else:ans+=cur[1]
        #print(u,flap,cur,ans)
        if ng:break

    if ng:print(-1)
    else:
        print(len(ans))
        print(*ans)


from bisect import bisect_left

N=int(input())
*A,=map(int,input().split())
INF=10**20
G=[[] for _ in range(N)]
ab = [tuple(map(int,input().split())) for _ in range(N-1)]
for a,b in ab:
  G[a-1].append(b-1)
  G[b-1].append(a-1)
  
def dfs(a0):
    seen =[0]*len(G)
    todo = [~a0, a0]
    while todo:
        a = todo.pop()
        if a >= 0:
            seen[a] = 1
            idx = bisect_left(lis,A[a])
            his[a] = (idx,lis[idx])
            lis[idx] = A[a]
            dp[a] = bisect_left(lis,INF)
            for b in G[a]:
                if seen[b]: continue
                todo.append(~b)
                todo.append(b)
        else:
          idx,val = his[~a]
          lis[idx] = val
    return
  
lis = [INF]*N
dp = [0]*N
his = {}
dfs(0)
print(*dp,sep="\n")

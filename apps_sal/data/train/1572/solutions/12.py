import sys
from collections import defaultdict
sys.setrecursionlimit(1000000)
def dfs(i,maxVal,maxDiff):
    visited[i]=True
    if not graph[i]:
        return maxDiff
    else:
        stack=[]
        for j in graph[i]:
            if not visited[j]:
                diff=max(maxDiff,maxVal-a[j])
                val=max(maxVal,a[j])
                stack.append(dfs(j,val,diff))
        return max(stack)

s=list(map(int,input().split()))
n=s[0]
a=s[1:n+1]
p=s[n+1:]
graph=defaultdict(list)
for i in range(n):
    graph[p[i]-1].append(i)
boss=graph[-2][0]
visited=[False]*n
print(dfs(boss,a[boss],0))

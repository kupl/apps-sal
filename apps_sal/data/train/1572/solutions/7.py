import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

arr=[int(x) for x in input().split()]

if arr[0]==1:
    print(0)
    return

p=[None]
for i in range(1,arr[0]+1):
    p.append(arr[i])
    
a=[None]
for i in range(arr[0]+1,2*arr[0]+1):
    a.append(arr[i])

graph=defaultdict(list)

n=len(a)-1
for i in range(1,n+1):
    if a[i]==-1:
        source=i
        continue
    graph[a[i]].append((i,(p[a[i]]-p[i])))

def func(node):
    nonlocal res
    
    if len(graph[node])==0:
        return -10**9
    
    curr=-10**9
    for child in graph[node]:
        x=max(child[1],(func(child[0])+child[1]))
        curr=max(curr,x)
        res=max(curr,res)
    
    return curr    

res=-10**9
curr=func(source)
print(res)        
        
        
        


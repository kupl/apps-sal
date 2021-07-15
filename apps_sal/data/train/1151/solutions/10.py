# cook your dish here
from collections import defaultdict
l=[]


def DFSUtil(d, temp, v, visited):
    visited[v] = True
    temp.append(v)
    for i in d[v]:
        if visited[i] == False:
            # Update the list
            temp = DFSUtil(d,temp, i, visited)
    return temp
def connectedComponents(n):
    visited = []
    cc = []
    for i in range(n):
        visited.append(False)
    for v in range(n):
        if visited[v] == False:
            temp = []
            cc.append(DFSUtil(d,temp, v, visited))
    return cc
for _ in range(int(input())):
    n,m=list(map(int,input().split()))
    d=defaultdict(list)
    for i in range(m):
        x,y=list(map(int,input().split()))
        d[x].append(y)
        d[y].append(x)
    l.append(len(connectedComponents(n)))
for i in l:
    print(i)



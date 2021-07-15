from sys import stdin, stdout,setrecursionlimit
from collections import defaultdict,deque,Counter,OrderedDict
from heapq import heappop,heappush
import threading

n = int(stdin.readline())

graph = [set() for x in range(n)]

for x in range(n-1):
    a,b = [int(x) for x in stdin.readline().split()]
    a -= 1
    b -= 1

    graph[a].add(b)
    graph[b].add(a)

vals = [int(x) for x in stdin.readline().split()]

bruh = [(0,-1)]

for x in range(n):
    num,p = bruh[x]
    for y in graph[num]:
        if y != p:
            bruh.append((y,num))

result = [-1 for x in range(n)]

for v,parent in bruh[::-1]:
    nP = 0
    nN = 0
    for x in graph[v]:
        if x != parent:
            p,n = result[x]
            nP = max(nP,p)
            nN = max(nN, n)
    nN = max(nN, nP+vals[v])
    nP = max(nP, nN-vals[v])
            
    result[v] = (nP,nN)

ng, ps = result[0]

vals[0] += ps - ng

stdout.write(str(ng+ps))


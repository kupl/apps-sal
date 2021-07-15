import bisect, copy, heapq, math, sys
from collections import *
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
def celi(a,b):
    return -(-a//b)
sys.setrecursionlimit(5000000)
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

xy=list(map(int,input().split()))
n=int(input())
xyr=[list(map(int,input().split())) for i in range(n)]

def dijkstra(s,e):
    hq = [(0, s)]
    heapq.heapify(hq) # リストを優先度付きキューに変換
    cost = [float('inf')] * n # 行ったことのないところはinf
    cost[s] = 0 # 開始地点は0
    while hq:
        c, v = heapq.heappop(hq)
        if c > cost[v]: # コストが現在のコストよりも高ければスルー
            continue
        for d, u in e[v]:
            tmp = d + cost[v]
            if tmp < cost[u]:
                cost[u] = tmp
                heapq.heappush(hq, (tmp, u))
    return cost

################################
n,w = n,(n+2)*(n+1)//2 #n:頂点数　w:辺の数

edge = [[] for i in range(n+2)]
#edge[i] : iから出る道の[重み,行先]の配列
for i in range(n):
    for j in range(i+1,n):
        x1,y1,r1=xyr[i]
        x2,y2,r2=xyr[j]
        dis=math.sqrt((x2-x1)**2+(y2-y1)**2)
        edge[i+1].append((max(0,dis-r1-r2),j+1))
        edge[j+1].append((max(0,dis-r1-r2),i+1))
for i in range(n):
    x1,y1,r1=xyr[i]
    dis=math.sqrt((xy[0]-x1)**2+(xy[1]-y1)**2)
    edge[0].append((max(0,dis-r1),i+1))
    edge[i+1].append((max(0,dis-r1),0))
    dis=math.sqrt((xy[2]-x1)**2+(xy[3]-y1)**2)
    edge[n+1].append((max(0,dis-r1),i+1))
    edge[i+1].append((max(0,dis-r1),n+1))
edge[0].append((math.sqrt((xy[0]-xy[2])**2+(xy[1]-xy[3])**2),n+1))
edge[n+1].append((math.sqrt((xy[0]-xy[2])**2+(xy[1]-xy[3])**2),0))
# print(edge)
n=n+2
print(dijkstra(0,edge)[-1])

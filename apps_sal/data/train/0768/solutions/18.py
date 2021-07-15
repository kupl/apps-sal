from sys import stdin as stin,stdout as stout,setrecursionlimit as srl
from collections import defaultdict as dd,Counter,deque as dq 
#from heapq import heapify,heappush as hpu,heappop as hpo
#import math 
#import numpy
srl(10**6)
def get_ints():return map(int,stin.readline().split())
def get_list(): return list(map(int,stin.readline().split()))
def get_int(): return int(stin.readline())
def get_str(): return stin.readline()
def dfs(graph,u,parent):
    size,max_mex=0,0
    for i in graph[u]:
        if i==parent:
            continue 
        tmax,tsize=dfs(graph,i,u)
        max_mex=max(max_mex,tmax) 
        size+=tsize 
    return max_mex+size+1,size+1
for _ in range(get_int()):
    n=get_int()
    nums=get_list()
    graph=dd(list)
    for i in range(2,n+1):
        graph[nums[i-2]].append(i) 
    print(dfs(graph,1,1)[0])
    

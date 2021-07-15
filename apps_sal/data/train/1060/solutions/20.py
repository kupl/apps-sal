from functools import lru_cache
import sys
try:
    from cp import input
except:
    def input():
        return sys.stdin.readline()
try:
    import numpy as np
except:
    pass
import math
import copy
import random
from copy import deepcopy
# def input(): return sys.stdin.readline()
def itarr(arr): return list(range(len(arr)))
def mp(): return list(map(int, input().split()))
def lmp(): return list(map(int, input().strip().split()))
def inp(): return int(input())


MOD = 1000000007


sys.setrecursionlimit(100000)
sys.settrace
inf_p = float('inf')
inf_n = float('-inf')

dsu=[]

def find(n):
    if n==dsu[n]:
        return n
    tmp=find(dsu[n])
    dsu[n]=tmp
    return tmp

def union(a,b):
    a=find(a)
    b=find(b)
    if a!=b:
        dsu[b]=a

adj=[]
vis=[]
wt=[]
MAXE=0
MAXO=0
ans=0

def even_parity(n):
    return (bin(n)[2:].count('1')%2)==0
def odd_parity(n):
    return not even_parity(n)

def dfse(curr_node,p):
    nonlocal MAXE, MAXO,vis,ans

    for node in adj[curr_node]:
        if vis[node]==0 :
            if even_parity(wt[node-1]):
                dfs(node,num)
        
def dfso(curr_node,p):
    nonlocal MAXE, MAXO,vis,ans
    
    for node in adj[curr_node]:
        if vis[node]==0 :
            if odd_parity(wt[node-1]):
                dfs(node,num)

def main():
    n=inp()
    s=input().strip()
    if len(s)==0:
        s=input().strip
    ones=[0]* (n+1)
    zeros=[0]* (n+1)
    one =0 
    zero=0
    for i in range(len(s)):
        ones[i]=one
        zeros[i]=zero
        if s[i]=='1':
            one+=1
        else:
            zero+=1 
    tot=0
    # print(ones,zeros)
    for i in range(n-1,0,-1):
        if s[i]=='1':
            tot+=zeros[i]
        else:
            tot+=ones[i]
        # print(i)
    print(tot)

# main()
for i in range(inp()):
    main()
# cook your dish here


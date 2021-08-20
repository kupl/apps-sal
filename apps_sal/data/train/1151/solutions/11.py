"""

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

"""
from sys import stdin, stdout
import sys
import math
import time
import random
from functools import lru_cache
from collections import Counter
import heapq
'*****     *****\n *******   *******\n********* *********\n*******************\n *****************\n  ****TITLI******\n   *************\n    ***********\n     *********\n      *******\n       *****\n        ***\n         *'


def Update(X, AX, BX, CX, DX, k, n):
    for i in range(k, n):
        tem = (AX * X[i - 2] + BX * X[i - 1] + CX) % DX + 1
        X.append(tem)


def my_function():
    print('Hello from a function')


'def changeme( mylist ):\n   "This changes a passed list into this function"\n   mylist.append([1,2,3,4]);\n   print "Values inside the function: ", mylist\n   returnd=[art[i+1]-art[i] for i in range(na-1)]\n        y=list(set(d))\n        ns=float(\'-inf\')\n        p=1\n        while p<na:\n                d=art[p]-art[p-1]\n                smy=1\n                while p<na and(art[p]-art[p-1]==d):\n                       p+=1\n                       smy+=1\n                       ns=max(ns,smy)\n           s,v=map(int,input().split())\n            addEdge(adj,s,v)\n        DFS(adj,0,n)\n\ndef DFS_REC(adj,s,visited):\n    visited[s]=True\n    for s in adj[s]:\n        if not visited[s]:\n            DFS_REC(adj,s,visited)\ndef DFS(adj,src,n):\n    visited=[False]*n\n    ans=0\n    for i in range(n):\n        if not visited[i]:\n            ans+=1\n            DFS_REC(adj,i,visited)\n    print(ans)\ndef addEdge(adj,u,v):\n    adj[u].append(v)\n    adj[v].append(u)'


def a(adj, s, visited):
    visited[s] = True
    for s in adj[s]:
        if not visited[s]:
            a(adj, s, visited)


def b(adj, src, n):
    visited = [False] * n
    ans = 0
    for i in range(n):
        if not visited[i]:
            ans += 1
            a(adj, i, visited)
    print(ans)


def e(adj, s, v):
    adj[s].append(v)
    adj[v].append(s)


try:
    for _ in range(int(input())):
        (n, m) = list(map(int, input().split()))
        adj = [[] for i in range(n + 1)]
        for i in range(m):
            (s, v) = list(map(int, input().split()))
            e(adj, s, v)
        b(adj, 0, n)
except EOFError as e:
    print(e)

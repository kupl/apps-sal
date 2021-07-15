# cook your dish here
'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
"""*****     *****
 *******   *******
********* *********
*******************
 *****************
  ****TITLI******
   *************
    ***********
     *********
      *******
       *****
        ***
         *"""
import sys
from sys import stdin,stdout
import math
import time
import random
from functools import lru_cache
from collections import Counter
import heapq
#@lru_cache(maxsize=None) #for optimizing the execution time of callable objects/functions(placed above callable functions)
def Update(X,AX,BX,CX,DX,k,n):
    for i in range(k,n):
        tem=(((AX*X[i-2])+(BX*X[i-1])+CX)%DX)+1
        X.append(tem)
def my_function():
  print("Hello from a function")
        
        
        
        
"""def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print "Values inside the function: ", mylist
   returnd=[art[i+1]-art[i] for i in range(na-1)]
        y=list(set(d))
        ns=float('-inf')
        p=1
        while p<na:
                d=art[p]-art[p-1]
                smy=1
                while p<na and(art[p]-art[p-1]==d):
                       p+=1
                       smy+=1
                       ns=max(ns,smy)
           s,v=map(int,input().split())
            addEdge(adj,s,v)
        DFS(adj,0,n)

def DFS_REC(adj,s,visited):
    visited[s]=True
    for s in adj[s]:
        if not visited[s]:
            DFS_REC(adj,s,visited)
def DFS(adj,src,n):
    visited=[False]*n
    ans=0
    for i in range(n):
        if not visited[i]:
            ans+=1
            DFS_REC(adj,i,visited)
    print(ans)
def addEdge(adj,u,v):
    adj[u].append(v)
    adj[v].append(u)"""
def a(adj,s,visited):
    visited[s]=True
    for s in adj[s]:
        if not visited[s]:
            a(adj,s,visited)
def b(adj,src,n):
    visited=[False]*n
    ans=0
    for i in range(n):
        if not visited[i]:
            ans+=1
            a(adj,i,visited)
    print(ans)




def e(adj,s,v):
    adj[s].append(v)
    adj[v].append(s)

try:
    for _ in range(int(input())):
        n,m=list(map(int,input().split()))
        adj=[[] for i in range(n+1)]
        for i in range(m):
            s,v=list(map(int,input().split()))
            e(adj,s,v)
        b(adj,0,n)
       
       















   
       
       
   
       
       
       
               
        
except EOFError as e:
    print(e)


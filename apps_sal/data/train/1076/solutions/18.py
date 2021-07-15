# cook your dish here
import numpy as np

def add(adj,a,b,n):
    adj[a,b] = adj[b,a] = 1
    for i in range(n):
        if adj[a,i]!=-10 and a!=i and b!=i and adj[b,i]==-10:
            adj[b,i] = adj[a,i] + 1
            adj[i,b] = adj[b,i]
    for i in range(n):
        if adj[b,i]!=-10 and b!=i and a!=i and adj[a,i]==-10:
            adj[a,i] = adj[b,i] + 1
            adj[i,a] = adj[a,i]
    return adj

t = int(input())
while t>0 :
    n,q = map(int,input().split())
    adj = np.zeros((n,n),dtype = 'int')
    adj += np.array([-10])
    for i in range(n):
        adj[i,i] = 0
    for i in range(1,n):
        a,b = map(int,input().split())
        adj = add(adj,a-1,b-1,n)
    for _ in range(q):
        a,da,b,db = map(int,input().split())
        x = -1
        for i in range(n):
            if adj[a-1,i] == da and adj[b-1,i] == db:
                x = i + 1
                break
        print(x)
    t -= 1

'''
Hey  why peeping here -_'_- ?
I believe on myself and I will achieve
this->author = Fuad Ashraful Mehmet, CSE ,University of Asia Pacific
Todo:
'''
import sys
input=sys.stdin.readline
from itertools import groupby
from collections import deque

R=lambda:map(int,input().split())
I=lambda:int(input())
S=lambda:input().rstrip('\n')
L=lambda:list(R())

def HalfDead():
    n,m=R()
    g=dict()
    for i in range(1,n+1):
        g[i]=dict()
    
    for i in range(m):
        u,v,c=R()
        g[u][v]=c
        g[v][u]=c
    #print("here")
    color=[0]*(n+2)
    color[1]=1

    dq=deque()
    dq.append(1)

    while dq:
        frm=dq.popleft()

        for to,c in g[frm].items():

            if color[to]==0:
                if color[frm]!=c:
                    color[to]=c
                else:
                    if c==n:
                        color[to]=1
                    else:
                        color[to]=c+1
            
                dq.append(to)
    

    for i in range(n):
        print(color[i+1])
    return

def __starting_point():
    #for _ in range(I()):
    HalfDead()
__starting_point()

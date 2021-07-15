from collections import deque
import sys
def inp():
    return sys.stdin.readline().strip()
for _ in range(int(inp())):
    n=int(inp())
    s=inp()
    ct=0
    mn=0
    for i in s:
        if i=='(':
            ct+=1 
        else:
            ct-=1
        mn=min(ct,mn)
    print(abs(mn))

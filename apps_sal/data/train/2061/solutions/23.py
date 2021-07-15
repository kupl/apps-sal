# coding: utf-8
# Your code here!
import sys
readline = sys.stdin.readline
read = sys.stdin.read


#a = int(readline())
#n,k = map(int, readline().split())

def solve1(a,b,c,d,e,f,cx,cy,x,y):
    if x==y:
        if x==0:
            if cx==cy==0:
                return 0
            else:
                return 1
        elif cx==cy==x+1:
            return 2*x+2
        else:
            return 2*x+1
    elif x < y:
        if cy==y:
            return 2*y
        else:
            return 2*y+1
    else:
        if cx==x:
            return 2*x
        else:
            return 2*x+1

def solve2(a,b,c,d,e,f):
    cx = sorted([a,c,e])[1]
    cy = sorted([b,d,f])[1]
    x = min(a,c,e)
    y = min(b,d,f)
    if x > y:
        if cx==x:
            return 2*x
        else:
            return 2*x+1
    else:
        if cy==y:
            return 2*y+1
        else:
            return 2*y+2
        

def solve3(a,b,c,d,e,f):
    cx = sorted([a,c,e])[1]
    cy = sorted([b,d,f])[1]
    x = min(a,c,e)
    y = min(b,d,f)
    if x != y:
        v = max(x,y)
        if cx == v+1 or cy == v+1:
            return 2*(v+1)
        else:
            return 2*(v+1)-1
    else:
        if cx == cy == x+1:
            return 2*(x+1)+1
        else:
            return 2*(x+1)


def solve():
    a,b,c,d,e,f = list(map(int, readline().split()))
    cx = sorted([a,c,e])[1]
    cy = sorted([b,d,f])[1]
    x = min(a,c,e)
    y = min(b,d,f)
    
    if x >= 0 and y >= 0:
        return solve1(a,b,c,d,e,f,cx,cy,x,y),1
    elif x >= 0:
        return solve2(a,-b,c,-d,e,-f),2
    elif y >= 0:
        return solve2(b,-a,d,-c,f,-e),22
    else:
        return solve3(-a,-b,-c,-d,-e,-f),3
            


T = int(readline())
for _ in range(T):
    print((solve()[0]))





from heapq import *
class Maxheap:
    def __init__(_): _.h = []
    def add(_, v): heappush(_.h, -v)
    def top(_): return -_.h[0]
    def pop(_): return -heappop(_.h)

class Graph:
    def __init__(_):
        _.change = Maxheap() # increment slope at ...
        _.change.add(-10**18)
        _.a = _.y = 0 # last line has slope a, starts from y
        _.dx = 0      # the whole graph is shifted right by ...
    def __repr__(_): return f"<{[x+_.dx for x in _.change]}; {_.a} {_.y}>"
    
    def shiftx(_, v): _.dx+= v
    def shifty(_, v): _.y+= v
    def addleft(_, v):
        if _.change.top() < v-_.dx:
            dx = v-_.dx - _.change.top()
            _.y+= _.a*dx
        _.change.add(v-_.dx)
    def addright(_, v):
        if _.change.top() < v-_.dx:
            dx = v-_.dx - _.change.top()
            _.y+= _.a*dx; _.a+= 1
            _.change.add(v-_.dx)
            return
        _.change.add(v-_.dx)
        _.a+= 1; _.y+= _.change.top()-(v-_.dx)
    def cutright(_):
        dx = _.change.pop()-_.change.top()
        _.a-= 1; _.y-= _.a*dx
 
n = int(input())
G = Graph()
for x in map(int,input().split()):
    G.shiftx(1)
    G.addleft(x)
    G.addright(x)
    while G.a > 0: G.cutright()
print(G.y)

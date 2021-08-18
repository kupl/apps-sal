from bisect import insort


class Graph:
    def __init__(_):
        _.change = [-10**27]
        _.a = _.y = 0
        _.dx = 0

    def __repr__(_): return f"<{[x+_.dx for x in _.change]}; {_.a} {_.y}>"

    def shiftx(_, v): _.dx += v
    def shifty(_, v): _.y += v

    def addleft(_, v):
        if _.change[-1] < v - _.dx:
            dx = v - _.dx - _.change[-1]
            _.y += _.a * dx
        insort(_.change, v - _.dx)

    def addright(_, v):
        if _.change[-1] < v - _.dx:
            dx = v - _.dx - _.change[-1]
            _.y += _.a * dx
            _.a += 1
            insort(_.change, v - _.dx)
            return
        insort(_.change, v - _.dx)
        _.a += 1
        _.y += _.change[-1] - (v - _.dx)

    def cutright(_):
        dx = _.change.pop() - _.change[-1]
        _.a -= 1
        _.y -= _.a * dx


n = int(input())
G = Graph()
for x in map(int, input().split()):
    G.shiftx(1)
    G.addleft(x)
    G.addright(x)
    while G.a > 0:
        G.cutright()
print(G.y)

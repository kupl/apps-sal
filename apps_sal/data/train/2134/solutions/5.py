class vertex:

    def __init__(self, v, sv, av=0):
        self.v = v
        self.sv = sv
        self.av = av
        self.child = []

    def sve(self):
        if self.child == []:
            return t.vert[pa[self.v - 2]].sv
        l = [t.vert[i].sv for i in self.child]
        return min(l)


class tree:

    def __init__(self):
        self.vert = {}


sum = 0
t = tree()
n = int(input())
pa = list(map(int, input().split()))
s = list(map(int, input().split()))
for i in range(1, n + 1):
    t.vert[i] = vertex(i, s[i - 1])
for i in range(n - 1):
    par = pa[i]
    t.vert[par].child.append(i + 2)
for i in range(1, n + 1):
    if t.vert[i].sv == -1:
        t.vert[i].sv = t.vert[i].sve()
for i in range(2, n + 1):
    k = t.vert[i].sv - t.vert[pa[t.vert[i].v - 2]].sv
    if k < 0:
        sum = -1
        break
    else:
        t.vert[i].av = k
if sum == -1:
    print(-1)
else:
    r = s[0]
    for i in range(2, n + 1):
        r += t.vert[i].av
    print(r)

n = int(input())


class Tree:
    height = 1

    def __init__(self, parent=None):
        self.nodes = []
        self.s = -1
        self.a = -1
        self.parent = parent
        if parent:
            self.height = parent.height + 1
            parent.nodes.append(self)


trs = [Tree()]
for i in map(int, input().split()):
    trs.append(Tree(trs[i - 1]))
for (i, s) in enumerate(map(int, input().split())):
    trs[i].s = s
trs.sort(key=lambda x: x.height)
trs[0].a = trs[0].s
res = trs[0].a
try:
    for t in trs[1:]:
        if t.s == -1:
            t.a = min([x.s - t.parent.s for x in t.nodes], default=0)
            t.s = t.a + t.parent.s
        else:
            t.a = t.s - t.parent.s
        if t.a < 0:
            raise
        res += t.a
    print(res)
except:
    print(-1)

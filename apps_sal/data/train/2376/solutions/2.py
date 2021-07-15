def crop_set(s, n):
    new = set()
    it = iter(s)
    for i in range(n):
        new.add(next(it))
    return new


class Vertex:
    __slots__ = ("vertexes", "leaves", "graph")

    def __init__(self, graph):
        self.vertexes = set()
        self.leaves = 0
        self.graph = graph

    def try_to_leave(self):
        if len(self.vertexes) + self.leaves == 1:
            if self.vertexes:
                parent = self.vertexes.pop()
                parent.vertexes.remove(self)
                parent.leaves += 1
                parent.update()
                self.vertexes.add(parent)

    def update(self):
        self.graph[self] = self.leaves


class Tree:
    def __init__(self, n, k):
        self.k = k
        self.lc = [set() for _ in range(n // k + 1)]
        self.dlc = dict()
        self.max = 0

    def add_vertex(self, v):
        self.dlc[v] = 0
        self.lc[0].add(v)
        v.update()

    def __setitem__(self, key, value):
        value = value // self.k

        if self.max == self.dlc[key] > value:
            self.lc[self.max].discard(key)
            while not self.lc[self.max]:
                self.max -= 1
        else:
            self.lc[self.dlc[key]].discard(key)

        if value > self.max:
            self.max = value
        self.dlc[key] = value
        self.lc[value].add(key)


def to_int_decrement(s):
    return int(s) - 1


def solve():
    n, k = list(map(int, input().split()))
    tree = Tree(n, k)
    graph = [Vertex(tree) for _ in range(n)]

    for _ in range(n - 1):
        a, b = list(map(to_int_decrement, input().split()))
        graph[a].vertexes.add(graph[b])
        graph[b].vertexes.add(graph[a])

    if k == 1:
        print(n - 1)
        return

    for v in graph:
        tree.add_vertex(v)
    for v in graph:
        v.try_to_leave()

    c = 0
    while tree.max > 0:
        v = tree.lc[tree.max].pop()
        c += v.leaves // k
        v.leaves -= v.leaves // k * k
        v.try_to_leave()
        v.update()
    print(c)


for _ in range(int(input())):
    solve()


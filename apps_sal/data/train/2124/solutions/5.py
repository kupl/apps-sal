from collections import deque


class Dinic():
    def __init__(self, listEdge, s, t):
        self.s = s
        self.t = t
        self.graph = {}
        self.maxCap = 1000000

        for e in listEdge:

            if e[0] not in self.graph:
                self.graph[e[0]] = []

            if e[1] not in self.graph:
                self.graph[e[1]] = []
            self.graph[e[0]].append([e[1], e[2], len(self.graph[e[1]])])
            self.graph[e[1]].append([e[0], 0, len(self.graph[e[0]]) - 1])

        self.N = len(self.graph.keys())

    def bfs(self):
        self.dist = {}
        self.dist[self.s] = 0
        self.curIter = {node: [] for node in self.graph}

        Q = deque([self.s])

        while(len(Q) > 0):
            cur = Q.popleft()

            for index, e in enumerate(self.graph[cur]):
                if e[1] > 0 and e[0] not in self.dist:
                    self.dist[e[0]] = self.dist[cur] + 1
                    self.curIter[cur].append(index)
                    Q.append(e[0])

    def findPath(self, cur, f):
        if cur == self.t:
            return f

        while len(self.curIter[cur]) > 0:
            indexEdge = self.curIter[cur][-1]
            nextNode = self.graph[cur][indexEdge][0]
            remainCap = self.graph[cur][indexEdge][1]
            indexPreEdge = self.graph[cur][indexEdge][2]

            if remainCap > 0 and self.dist[nextNode] > self.dist[cur]:
                flow = self.findPath(nextNode, min(f, remainCap))

                if flow > 0:
                    self.path.append(cur)
                    self.graph[cur][indexEdge][1] -= flow
                    self.graph[nextNode][indexPreEdge][1] += flow
                    return flow
            self.curIter[cur].pop()

        return 0

    def maxFlow(self):
        maxflow = 0
        flow = []

        while(True):
            self.bfs()

            if self.t not in self.dist:
                break

            while(True):
                self.path = []
                f = self.findPath(self.s, self.maxCap)
                if f == 0:
                    break

                flow.append(f)
                maxflow += f

        return maxflow

    def residualBfs(self):
        Q = deque([self.s])
        side = {self.s: 's'}

        while(len(Q) > 0):
            cur = Q.popleft()

            for index, e in enumerate(self.graph[cur]):
                if e[1] > 0 and e[0] not in side:
                    Q.append(e[0])
                    side[e[0]] = 's'

        S = []
        T = []
        for x in self.graph:
            if x in side:
                S.append(x)
            else:
                T.append(x)
        return set(S), set(T)


def is_ok(val, flow, X):
    num = 0
    for f in flow:
        num += f // val

    if num >= X:
        return True
    return False


n, m, X = map(int, input().split())
edge = [list(map(int, input().split())) for _ in range(m)]

l, r = 0, 1000000

while r - l > 1e-9:
    md = (r + l) / 2
    edge_ = [[u, v, w // md] for u, v, w in edge]
    g = Dinic(edge_, 1, n)
    maxflow = g.maxFlow()

    if maxflow >= X:
        l = md
    else:
        r = md

print(X * r)

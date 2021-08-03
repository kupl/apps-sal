from sys import setrecursionlimit
setrecursionlimit(10**6)


class Graph:
    def __init__(self, V):
        self.graph = [[] for i in range(V + 1)]
        self.Visited = set()
        self.height = 1

    def addEdges(self):
        arr = [int(x) for x in input().split()]
        for i in range(len(arr)):
            self.graph[i + 1].append(arr[i] - 1)
            self.graph[arr[i] - 1].append(i + 1)

    def DFS(self, Node):
        self.Visited.add(Node)
        if len(self.graph[Node]) == 0:
            return 1, 1
        node = 1
        mex = 1
        for each in self.graph[Node]:
            if each not in self.Visited:
                n1, m1 = self.DFS(each)
                node += n1
                mex = max(m1, mex)

        return node, mex + node


for _ in range(int(input())):
    V = int(input())
    gra = Graph(V)
    gra.addEdges()
    # print(gra.graph)
    x, y = gra.DFS(0)
    print(y - 1)
    # print(height*height)
    # print((gra.height*(gra.height+1))//2)

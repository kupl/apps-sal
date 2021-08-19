class Graph:

    def __init__(self):
        self.numVertices = None
        self.numEdges = None
        self.neighbors = None
        self.loadGraph()

    def loadGraph(self):
        (self.numVertices, self.numEdges) = list(map(int, input().split()))
        self.numVertices += 1
        self.neighbors = tuple((list() for vertex in range(self.numVertices)))
        self.groups = (set(), set())
        for edge in range(self.numEdges):
            (vertex1, vertex2) = list(map(int, input().split()))
            self.neighbors[vertex1].append(vertex2)
            self.neighbors[vertex2].append(vertex1)

    def isBipartite(self):
        return all((self.isBipartiteComponent(vertex) for vertex in range(1, self.numVertices) if self.groupOf(vertex) == None))

    def isBipartiteComponent(self, vertex):
        if len(self.neighbors[vertex]) == 0:
            return True
        self.groups[0].add(vertex)
        queue = [vertex]
        while queue:
            vertex = queue.pop()
            groupOfVertex = self.groupOf(vertex)
            for neighbor in self.neighbors[vertex]:
                groupOfNeighbor = self.groupOf(neighbor)
                if groupOfNeighbor == groupOfVertex:
                    return False
                elif groupOfNeighbor == None:
                    self.groups[not groupOfVertex].add(neighbor)
                    queue.append(neighbor)
        return True

    def groupOf(self, vertex):
        return 0 if vertex in self.groups[0] else 1 if vertex in self.groups[1] else None


def solve():
    graph = Graph()
    if graph.isBipartite():
        for group in graph.groups:
            print(len(group))
            print(' '.join(map(str, group)))
    else:
        print(-1)


def __starting_point():
    solve()


__starting_point()

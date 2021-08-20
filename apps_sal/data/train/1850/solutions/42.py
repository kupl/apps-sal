class Solution:

    def __init__(self):
        self.children = []
        self.pathSums = []

    def buildGraph(self, edges):
        graph = dict()
        for edge in edges:
            n1 = edge[0]
            n2 = edge[1]
            if n1 not in graph:
                graph[n1] = set([n2])
            else:
                graph[n1].add(n2)
            if n2 not in graph:
                graph[n2] = set([n1])
            else:
                graph[n2].add(n1)
        return graph

    def postOrder(self, graph, v, parent):
        for child in graph[v]:
            if child != parent:
                self.postOrder(graph, child, v)
                self.children[v] += self.children[child]
                self.pathSums[v] += self.children[child] + self.pathSums[child]

    def preOrder(self, graph, v, parent):
        for child in graph[v]:
            if child != parent:
                self.pathSums[child] = self.pathSums[v] + (len(graph) - self.children[child]) - self.children[child]
                self.preOrder(graph, child, v)

    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        if N == 0:
            return []
        elif N == 1:
            return [0]
        graph = self.buildGraph(edges)
        self.children = [1 for node in graph]
        self.pathSums = [0 for node in graph]
        self.postOrder(graph, 0, -1)
        self.preOrder(graph, 0, -1)
        return self.pathSums

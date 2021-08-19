import queue as qu


class Answer:

    def __init__(self, N):
        self.countarray = [0] * N
        self.ansarray = [0] * N


class Solution:

    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        if N == 1:
            return [0]
        o = Answer(N)
        graph = {}
        for i in range(N):
            graph[i] = []
        for i in range(len(edges)):
            graph.get(edges[i][0]).append(edges[i][1])
            graph.get(edges[i][1]).append(edges[i][0])
        self.count_generator(0, -1, o, graph)
        self.bfs(N, graph, o)
        self.generate_answer(0, -1, o, graph, N)
        return o.ansarray

    def generate_answer(self, node, parent, o, graph, N):
        if parent != -1:
            o.ansarray[node] = o.ansarray[parent] - o.countarray[node] + (N - o.countarray[node])
        for neighbor in graph.get(node):
            if neighbor == parent:
                continue
            self.generate_answer(neighbor, node, o, graph, N)

    def bfs(self, N, graph, o):
        visited = [False] * N
        q = qu.Queue()
        q.put([0, 0])
        while q.qsize():
            count = q.qsize()
            while count > 0:
                rem = q.get()
                if visited[rem[0]] == True:
                    continue
                else:
                    visited[rem[0]] = True
                count -= 1
                o.ansarray[0] += rem[1]
                for i in graph.get(rem[0]):
                    if visited[i] == False:
                        q.put([i, rem[1] + 1])

    def count_generator(self, node, parent, o, graph):
        for neighbor in graph.get(node):
            if neighbor == parent:
                continue
            self.count_generator(neighbor, node, o, graph)
            o.countarray[node] += o.countarray[neighbor]
        o.countarray[node] += 1

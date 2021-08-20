from collections import deque


class Solution:

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = {i: [] for i in range(1, N + 1)}
        for (a, b) in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        self.is_possible = True
        self.visited = [0] * (N + 1)
        self.color = [0] * (N + 1)
        for i in range(1, N + 1):
            if not self.visited[i]:
                self.color[i] = 1
                self.traverse(graph, i)
        return self.is_possible

    def traverse(self, graph, node):
        queue = deque([node])
        while queue:
            node = queue.popleft()
            self.visited[node] = 1
            color = self.color[node]
            for neigh in graph[node]:
                if color == self.color[neigh]:
                    self.is_possible = False
                    return
                if not self.visited[neigh] and (not neigh in queue):
                    self.color[neigh] = -color
                    queue.append(neigh)

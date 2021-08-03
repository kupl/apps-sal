class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        self.graph = [[] for i in range(n)]
        for u, v in dislikes:
            self.graph[u - 1].append(v - 1)
            self.graph[v - 1].append(u - 1)

        self.groups = [None for i in range(n)]

        for i in range(n):
            if self.groups[i] == None:
                if not self.bfs(i):
                    return False

        return True

    def bfs(self, node):
        queue = [node]
        self.groups[node] = 0

        while queue:
            q = queue.pop(0)
            for node in self.graph[q]:
                if self.groups[node] == None:
                    self.groups[node] = self.groups[q] ^ 1
                    queue.append(node)
                elif self.groups[node] == self.groups[q]:
                    return False

        return True

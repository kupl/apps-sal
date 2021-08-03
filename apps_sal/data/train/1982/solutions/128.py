class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        dislikes.sort()
        graph = [[] for _ in range(N + 1)]

        disjoint = [None for _ in range(N + 1)]

        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        self.graph = graph
        self.disjoint = disjoint

        for i in range(1, N + 1):
            if not self.dfs(i):
                return False

        return True

    def dfs(self, start, color=None):
        if self.disjoint[start] is not None:
            return color is None or self.disjoint[start] == color

        color = True if color is None else color
        self.disjoint[start] = color
        for other in self.graph[start]:
            if not self.dfs(other, not color):
                return False
        return True

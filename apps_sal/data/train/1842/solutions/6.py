class Solution:

    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        if n == 1:
            return 1.0
        graph = collections.defaultdict(list)
        for (u, v) in edges:
            graph[u].append(v)
            graph[v].append(u)
        q = collections.deque()
        q.append((1, 1.0))
        visited = set()
        self.target = target
        return self.dfs(graph, 1, t, visited)

    def dfs(self, graph, i, t, visited):
        if t == 0 or (i != 1 and len(graph[i]) == 1):
            if i == self.target:
                return 1
            return 0
        result = 0
        visited.add(i)
        for j in graph[i]:
            if j not in visited:
                result += self.dfs(graph, j, t - 1, visited)
        if i == 1:
            return result / len(graph[i])
        else:
            return result / (len(graph[i]) - 1)

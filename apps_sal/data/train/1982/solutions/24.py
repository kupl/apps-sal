class Solution:

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(N + 1)]
        for (a, b) in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        visited = [0] * (N + 1)

        def go(node, prev, color):
            if visited[node] != 0:
                return visited[node] == color
            visited[node] = color
            for t in graph[node]:
                if t == prev:
                    continue
                if not go(t, node, -color):
                    return False
            return True
        for i in range(1, N + 1):
            if visited[i] == 0 and (not go(i, 0, 1)):
                return False
        return True

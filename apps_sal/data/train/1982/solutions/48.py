class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = []
        for person in range(N+1):
            graph.append([])
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        seen = {}
        for i in range(1, N+1):
            if i not in seen:
                if self.bfs(graph, i, seen) == False:
                    return False
        return True
    
    def bfs(self, graph, person, seen):
        q = [(person, 1)]
        while q:
            person, color = q.pop(0)
            if person in seen:
                if seen[person] != color:
                    return False
                continue
            seen[person] = color
            vertices = graph[person]
            for v in vertices:
                q.append((v, -color))
        return True

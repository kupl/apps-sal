class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:

        graph = {i: [] for i in range(1, N + 1)}

        for dislike in dislikes:
            u, v = dislike
            graph[u].append(v)
            graph[v].append(u)
        visited = collections.defaultdict(int)
        queue = collections.deque([])
        color = 0
        for i in range(1, N + 1):
            if i not in visited:
                queue.append(i)
                visited[i] = 0
            while queue:
                node = queue.popleft()
                clr = visited[node]
                for nei in graph[node]:
                    if nei not in visited:
                        visited[nei] = ~clr
                        queue.append(nei)
                    else:
                        if visited[nei] == clr:
                            return False
        return True

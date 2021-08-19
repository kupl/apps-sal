class Solution:

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        (NOT_COLORED, RED, BLUE) = (0, 1, -1)
        colors = {p: NOT_COLORED for p in range(1, N + 1)}
        graph = collections.defaultdict(list)

        def dfs(person, color):
            colors[person] = color
            for neighbor in graph[person]:
                if colors[neighbor] == color:
                    return False
                if colors[neighbor] == NOT_COLORED and (not dfs(neighbor, -color)):
                    return False
            return True
        for (x, y) in dislikes:
            graph[x].append(y)
            graph[y].append(x)
        for i in range(1, N + 1):
            if colors[i] == NOT_COLORED and (not dfs(i, RED)):
                return False
        return True

class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        G = [[] for _ in range(n)]
        for x, y in red_edges:
            G[x].append((y, 1))
        for x, y in blue_edges:
            G[x].append((y, -1))

        def bfs(target):
            if target == 0:
                return 0
            q = deque([(y, color, 1) for y, color in G[0]])
            visited = set()
            while q:
                l = len(q)
                curr, color, level = q.popleft()
                visited.add((curr, color))
                if curr == target:
                    return level
                for y, z in G[curr]:
                    if z != color and (y, z) not in visited:
                        q.append((y, z, level + 1))
            return -1
        return [bfs(i) for i in range(0, n)]

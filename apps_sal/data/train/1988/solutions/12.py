from collections import defaultdict, deque


class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for to, frm in red_edges:
            graph[to] += [[frm, 1]]
        for to, frm in blue_edges:
            graph[to] += [[frm, 0]]

        paths = [-1] * n
        visited = set()
        queue = deque()
        queue.append((0, None, 0))

        while queue:
            curr, color, path = queue.popleft()
            if paths[curr] == -1:
                paths[curr] = path

            for v, c in graph[curr]:
                if (v, c) not in visited and (color == None or c != color):
                    queue.append((v, c, path + 1))
                    visited.add((v, c))
        return paths

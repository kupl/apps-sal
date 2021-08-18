import numpy as np


class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)
        for src, des in red_edges:
            graph[src].add((des, 1))

        for src, des in blue_edges:
            graph[src].add((des, 2))
        seen = set()

        res = [-1] * n

        q = [(0, 0, 1), (0, 0, 2)]

        while q:
            nextq = []
            for cur, dist, color in q:
                if res[cur] == -1:
                    res[cur] = dist
                for neighbor, nextColor in graph[cur]:
                    if nextColor != color and (cur, neighbor, nextColor) not in seen:
                        nextq.append((neighbor, dist + 1, nextColor))
                        seen.add((cur, neighbor, nextColor))
            q = nextq

        return res

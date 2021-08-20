import collections
from heapq import heappop, heappush


class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf') for _ in range(n)] for _ in range(n)]
        graph = collections.defaultdict(list)
        for (u, v, w) in edges:
            dist[u][v] = dist[v][u] = w
            graph[u].append(v)
            graph[v].append(u)
        for i in range(n):
            dist[i][i] = 0
        visited = set()
        for i in range(n):
            stack = [(0, i)]
            while stack:
                (k, j) = heappop(stack)
                if (i, j) not in visited and k <= distanceThreshold:
                    visited.add((i, j))
                    for neigh in graph[j]:
                        dist[i][neigh] = min(dist[i][neigh], k + dist[j][neigh])
                        heappush(stack, (dist[i][neigh], neigh))
        print(dist)
        ans = None
        maxi = float('inf')
        for i in range(n):
            temp = 0
            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    temp += 1
            if temp <= maxi:
                maxi = temp
                ans = i
        return ans

import numpy as np


class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = np.inf * np.ones((n, n))
        for k in range(len(edges)):
            dist[edges[k][0], edges[k][1]] = edges[k][2]
            dist[edges[k][1], edges[k][0]] = edges[k][2]
        for k in range(n):
            dist[k, k] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i, j] > dist[i, k] + dist[j, k]:
                        dist[i, j] = dist[i, k] + dist[j, k]
        dist[dist > distanceThreshold] = 0
        dist[dist > 0] = 1
        number = np.sum(dist, 1)
        curr_min = n
        index = 0
        for k in range(n):
            if number[k] <= curr_min:
                curr_min = number[k]
                index = k
        return index

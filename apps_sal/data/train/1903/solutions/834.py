import numpy
from sortedcontainers import SortedList


# Definition for a binary tree node.
class Solution:

    def minKey(self, num_v, key, mstSet):

        min = sys.maxsize
        for v in range(num_v):
            if key[v] < min and not mstSet[v]:
                min = key[v]
                min_index = v

        return min, min_index

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        result = 0
        num_v = len(points)
        dims = (num_v, num_v)
        graph = numpy.zeros(dims)
        for i in range(num_v):
            for j in range(i, num_v):
                delta_x = abs(points[i][0] - points[j][0])
                delta_y = abs(points[i][1] - points[j][1])
                graph[i][j] = graph[j][i] = delta_x + delta_y

        parent = [None] * num_v
        parent[0] = -1  # First node is always the root of

        key = [sys.maxsize] * num_v
        key[0] = 0

        mstSet = [False] * num_v

        for cout in range(num_v):
            tmp, u = self.minKey(num_v, key, mstSet)
            result += tmp
            mstSet[u] = True

            for v in range(num_v):

                if graph[u][v] > 0 and not mstSet[v] and key[v] > graph[u][v]:
                    key[v] = graph[u][v]
                    parent[v] = u

        return int(result)

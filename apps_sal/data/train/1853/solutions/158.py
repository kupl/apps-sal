from collections import defaultdict
from heapq import heapify, heappush, heappop
import math


class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        for i in range(len(edges)):
            graph[edges[i][0]].append([edges[i][1], edges[i][2]])
            graph[edges[i][1]].append([edges[i][0], edges[i][2]])
        res = [0] * n
        for i in range(n):
            visited = [False] * n
            distance = [math.inf] * n
            distance[i] = 0
            stack = [[0, i]]
            count = 0
            while len(stack) != 0:
                p = heappop(stack)
                if p[0] > distanceThreshold:
                    break
                visited[p[1]] = True
                for node in graph[p[1]]:
                    if visited[node[0]] == False:
                        if p[0] + node[1] < distance[node[0]]:
                            distance[node[0]] = distance[p[1]] + node[1]
                            heappush(stack, [distance[node[0]], node[0]])
            count = 0
            for j in range(n):
                if visited[j] == True:
                    count += 1
            res[i] = count - 1
        m = math.inf
        pos = 0
        for i in range(n):
            if res[i] <= m:
                m = res[i]
                pos = i
        return pos

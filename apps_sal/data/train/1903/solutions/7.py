import queue
import sys

class Solution:
    def minCostConnectPoints(self, p: List[List[int]]) -> int:
        n = len(p)
        graph = [[] for i in range(n + 1)]
        dist = [1000000000 for i in range(n + 1)]
        for i in range(len(p)):
            for j in range(len(p)):
                if i == j: 
                    continue
                graph[i].append((j, abs(p[i][0] - p[j][0]) + abs(p[i][1] - p[j][1])))
                graph[j].append((i, abs(p[i][0] - p[j][0]) + abs(p[i][1] - p[j][1])))
        pq = queue.PriorityQueue()
        pq.put((0, 0))
        dist[0] = 0
        res = 0
        while pq.empty() == False:
            (du, u) = pq.get()
            if du != dist[u]:
                continue

            dist[u] = 0
            res += du
            for (v, uv) in graph[u]:
                if dist[v] > uv:
                    dist[v] = uv
                    pq.put((uv, v))
        return res                

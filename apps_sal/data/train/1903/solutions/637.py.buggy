from queue import PriorityQueue

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        graph = [[-1] * n for _ in range(n)]
        for u in range(n):
            for v in range(n):
                graph[u][v] = abs(points[u][0]-points[v][0]) + abs(points[u][1]-points[v][1])
        
        res = 0
        dists = [float(\"inf\")] * n
        parents = [-1] * n
        mst = set()
        pq = PriorityQueue()
        dists[0] = 0
        pq.put([0, 0])
        while len(mst) < n:
            dist, u = pq.get()
            if u not in mst:
                res += dist
                mst.add(u)
            for v in range(n):
                if dists[v] > graph[u][v]:
                    dists[v] = graph[u][v]
                    parents[v] = u
                    pq.put([dists[v], v])
        return res
        
        

from queue import PriorityQueue as PQ
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dist = [[] for _ in range(n)]
        for i in range(n):
            xi, yi = points[i]
            for j in range(i+1, n):
                xj, yj = points[j]
                d = abs(xi-xj) + abs(yi-yj)
                dist[i].append((j, d))
                dist[j].append((i, d))
        chosen = set([0])
        pq = PQ()
        seen = [0]*n
        for i, d in dist[0]:
            pq.put((d, i))
            seen[i] = d
        ans, edges = 0, 0
        while not pq.empty() and edges < n-1:
            d, i = pq.get()
            if i not in chosen:
                chosen.add(i)
                ans += d
                edges += 1
                for j, dj in dist[i]:
                    if j not in chosen and dj < seen[j]:
                        pq.put((dj, j))
                        seen[j] = dj
        return ans


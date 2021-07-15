class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        mst = set()
        mst.add(0)
        md = 0
        pq = []
        for i in range(n):
            if i not in mst:
                distance = abs(points[0][0] - points[i][0]) + abs(points[0][1] - points[i][1])
                heapq.heappush(pq, (distance, 0, i))
        
        while pq:
            distance, a, b = heapq.heappop(pq)
            if b not in mst:
                mst.add(b)
                md += distance
                for i in range(n):
                    if i not in mst:
                        distance = abs(points[b][0] - points[i][0]) + abs(points[b][1] - points[i][1])
                        heapq.heappush(pq, (distance, b, i))
        
        return md

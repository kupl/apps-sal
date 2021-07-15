class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n, dists = len(points), collections.defaultdict(list)
        if n <= 1:
            return 0
        for i in range(n-1):
            for j in range(i+1, n):
                dist = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                dists[i].append((dist, j))
                dists[j].append((dist, i))
        res, visited, cnt, heap = 0, [0]*n, 1, dists[0]
        visited[0] = 1
        heapq.heapify(heap)
        while heap:
            dist, i = heappop(heap)
            if not visited[i]:
                res += dist
                cnt += 1
                for ele in dists[i]:
                    heappush(heap, ele)
                visited[i] = 1
            if cnt == n:
                return res

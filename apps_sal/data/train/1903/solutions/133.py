class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def dist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        ans = 0
        d = collections.defaultdict(list)
        for (i, p1) in enumerate(points):
            for (j, p2) in enumerate(points):
                if i != j:
                    cost = dist(p1, p2)
                    d[i].append((cost, j))
                    d[j].append((cost, i))
        heap = d[0]
        heapq.heapify(heap)
        n = len(points)
        visited = [0] * n
        visited[0] = 1
        count = 1
        while heap:
            (cost, j) = heapq.heappop(heap)
            if not visited[j]:
                visited[j] = 1
                count += 1
                ans += cost
                for item in d[j]:
                    heapq.heappush(heap, item)
            if count >= n:
                break
        return ans

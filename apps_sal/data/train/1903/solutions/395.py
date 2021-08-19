class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def get_dist(i, j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        (n, c) = (len(points), collections.defaultdict(list))
        for i in range(n):
            for j in range(i + 1, n):
                d = get_dist(i, j)
                c[i].append((d, j))
                c[j].append((d, i))
        (cnt, ans, visited, heap) = (1, 0, [0] * n, c[0])
        visited[0] = 1
        heapq.heapify(heap)
        while heap and cnt < n:
            (d, j) = heapq.heappop(heap)
            if not visited[j]:
                (visited[j], cnt, ans) = (1, cnt + 1, ans + d)
                for record in c[j]:
                    heapq.heappush(heap, record)
        return ans

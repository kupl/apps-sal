class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def manhattan(p1, p2): return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        n, dic = len(points), collections.defaultdict(list)

        for i in range(n):
            for j in range(i + 1, n):
                d = manhattan(points[i], points[j])
                dic[i].append((d, j))
                dic[j].append((d, i))

        cnt, ans, visited, heap = 1, 0, [0] * n, dic[0]
        visited[0] = 1
        heapq.heapify(heap)
        while heap:
            d, j = heapq.heappop(heap)
            if not visited[j]:
                visited[j], cnt, ans = 1, cnt + 1, ans + d
                for record in dic[j]:
                    heapq.heappush(heap, record)
            if cnt >= n:
                break
        return ans

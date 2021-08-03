class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        graph = collections.defaultdict(list)
        def mh(p1, p2): return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        for i in range(n):
            for j in range(i + 1, n):
                d = mh(points[i], points[j])
                graph[i].append((d, j))
                graph[j].append((d, i))
        cnt = 1
        ans = 0
        visited = [False] * n
        heap = graph[0]
        visited[0] = True
        heapq.heapify(heap)
        while heap:
            d, j = heapq.heappop(heap)
            if not visited[j]:
                visited[j] = True
                ans += d
                cnt += 1
                for nei in graph[j]:
                    heapq.heappush(heap, nei)
            if cnt >= n:
                break
        return ans

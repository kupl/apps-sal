class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def distance(p1, p2): return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        from collections import defaultdict
        n = len(points)
        c = defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                d = distance(points[i], points[j])
                c[i].append((d, j))
                c[j].append((d, i))
        visited = [False] * n
        answer = 0
        cnt = 0
        import heapq
        heap = c[0]
        visited[0] = True
        heapq.heapify(heap)
        while heap:
            d, j = heapq.heappop(heap)
            if visited[j] == False:
                visited[j] = True
                answer = answer + d
                cnt += 1
                for record in c[j]:
                    heapq.heappush(heap, record)

        return answer

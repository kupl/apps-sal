class Solution:

    def minCostConnectPoints(self, p: List[List[int]]) -> int:
        (n, c) = (len(p), collections.defaultdict(list))
        for i in range(n):
            for j in range(i + 1, n):
                d = abs(p[i][0] - p[j][0]) + abs(p[i][1] - p[j][1])
                c[i].append((d, j))
                c[j].append((d, i))
        (cnt, ans, visited, heap) = (1, 0, [0] * n, c[0])
        visited[0] = 1
        heapq.heapify(heap)
        while heap:
            (d, j) = heapq.heappop(heap)
            if not visited[j]:
                (visited[j], cnt, ans) = (1, cnt + 1, ans + d)
                for record in c[j]:
                    heapq.heappush(heap, record)
            if cnt >= n:
                break
        return ans

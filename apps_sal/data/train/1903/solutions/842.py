
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manh(x1, x2, y1, y2):
            return abs(x1 - x2) + abs(y1 - y2)

        visited = set()
        n = len(points)
        c = defaultdict(list)
        res = 0

        for i in range(n - 1):
            for j in range(1, n):
                d = manh(points[i][0], points[j][0], points[i][1], points[j][1])
                c[j].append((d, i))
                c[i].append((d, j))

        visited.add(0)
        heap = c[0]
        heapq.heapify(heap)
        cnt = 1

        while heap:
            d, x = heapq.heappop(heap)

            if x not in visited:
                visited.add(x)
                res += d
                cnt += 1
                for r in c[x]:
                    heapq.heappush(heap, r)
            if cnt >= n:
                break
        return res

import heapq


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def manhattan(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        (n, c) = (len(points), collections.defaultdict(list))
        for i in range(n):
            for j in range(i + 1, n):
                d = manhattan(points[i], points[j])
                c[i].append((d, j))
                c[j].append((d, i))
        visited = set()
        visited.add(0)
        res = 0
        heap = c[0]
        heapq.heapify(heap)
        while len(visited) < n:
            (d, j) = heapq.heappop(heap)
            if j not in visited:
                visited.add(j)
                res += d
                for record in c[j]:
                    heapq.heappush(heap, record)
        return res

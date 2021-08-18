class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        g = collections.defaultdict(list)
        n = len(points)
        for i in range(n):
            for j in range(n):
                if i != j:
                    g[i].append((manhattan(points[i], points[j]), j))

        heap = [(0, 0)]
        ans = 0
        visited = set()
        while heap:
            weight, to = heapq.heappop(heap)
            if to in visited:
                continue
            ans += weight
            visited.add(to)

            for cost, nei in g[to]:
                if nei not in visited:
                    heapq.heappush(heap, (cost, nei))

        return ans

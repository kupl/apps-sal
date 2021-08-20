class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def calculate_distance(x1, y1, x2, y2):
            return abs(x1 - x2) + abs(y1 - y2)
        res = 0
        n = len(points)
        visited = set()
        d = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i != j:
                    d[i].append((calculate_distance(points[i][0], points[i][1], points[j][0], points[j][1]), j))
                    d[j].append((calculate_distance(points[i][0], points[i][1], points[j][0], points[j][1]), i))
        heap = d[0]
        heapq.heapify(heap)
        visited.add(0)
        count = 1
        while heap and count < n:
            (dist, j) = heapq.heappop(heap)
            if j not in visited:
                visited.add(j)
                res += dist
                count += 1
                for r in d[j]:
                    heapq.heappush(heap, r)
        return res

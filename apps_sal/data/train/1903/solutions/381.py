class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def md(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        n = len(points)
        graph = defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                d = md(points[i], points[j])
                graph[i].append((d, j))
                graph[j].append((d, i))
        visited = {0}
        q = graph[0]
        heapq.heapify(q)
        res = 0
        while len(q) != 0:
            (d, j) = heapq.heappop(q)
            if j not in visited:
                visited.add(j)
                res += d
                for item in graph[j]:
                    heapq.heappush(q, item)
            if len(visited) == n:
                break
        return res

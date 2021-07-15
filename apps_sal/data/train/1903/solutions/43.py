class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return 0

        graph = defaultdict(list)

        for i in range(n):
            for j in range(n):
                if i != j:
                    dist = abs(points[i][0]-points[j][0]) + \\
                        abs(points[i][1]-points[j][1])
                    graph[i].append((j, dist))

        def mst(graph):
            total = 0
            seen = set()
            start = next(iter(graph))
            unseen = [(0, start)]
            while unseen:
                cost, node = heappop(unseen)
                if node not in seen:
                    seen.add(node)
                    total += cost
                    for nei, cost in graph[node]:
                        if nei not in seen:
                            heappush(unseen, (cost, nei))
            return total

        return mst(graph)

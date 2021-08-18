class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def build_graph(points):
            g = {i: {} for i in range(len(points))}
            for i in range(len(points)):
                for j in range(i + 1, len(points)):
                    dist = abs(points[j][0] - points[i][0]) + abs(points[j][1] - points[i][1])
                    g[i][j] = dist
                    g[j][i] = dist
            return g

        def min_span_tree(g):
            import heapq

            cost = 0
            min_heap = []
            heapq.heappush(min_heap, (0, 0))
            visited = set()

            while len(min_heap):
                nxt_cost, idx = heapq.heappop(min_heap)
                if idx in visited:
                    continue
                visited.add(idx)
                cost += nxt_cost

                for adj in g[idx]:
                    if adj not in visited:
                        heapq.heappush(min_heap, (g[idx][adj], adj))
            return cost

        g = build_graph(points)
        return min_span_tree(g)

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def getDist(p1, p2):
            # |xi - xj| + |yi - yj|
            xi, yi = p1
            xj, yj = p2
            return abs(xi - xj) + abs(yi - yj)

        graph = collections.defaultdict(list)
        for i in range(len(points)):
            for j in range(len(points)):
                graph[i].append((getDist(points[i], points[j]), j))
        start = res = 0
        visited = {start}
        min_heap = []
        for cost, adj in graph[start]:
            heapq.heappush(min_heap, (cost, adj))
        while len(visited) < len(points) + 1 and min_heap:
            cost, next_node = heapq.heappop(min_heap)
            if next_node not in visited:
                visited.add(next_node)
                res += cost
                for next_cost, adj in graph[next_node]:
                    if adj not in visited:
                        heapq.heappush(min_heap, (next_cost, adj))
        return res

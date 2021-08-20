class Solution:

    def minCostConnectPoints(self, points) -> int:
        graph = defaultdict(list)
        for i in range(len(points)):
            (x, y) = points[i]
            for j in range(len(points)):
                (x1, y1) = points[j]
                if i != j:
                    graph[i].append((abs(x - x1) + abs(y - y1), j))
        start = 0
        res = 0
        visited = {start}
        min_heap = []
        for (md, neighbor) in graph[start]:
            heapq.heappush(min_heap, (md, neighbor))
        while len(visited) < len(points):
            (md, next_node) = heapq.heappop(min_heap)
            if next_node not in visited:
                visited.add(next_node)
                res += md
                for (nxt_md, next_neighbor) in graph[next_node]:
                    if next_neighbor not in visited:
                        heapq.heappush(min_heap, (nxt_md, next_neighbor))
        return res

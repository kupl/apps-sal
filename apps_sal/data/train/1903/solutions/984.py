class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for i in range(len(points)):
            x0, y0 = points[i]
            for j in range(i+1, len(points)):
                x1, y1 = points[j]
                dist = abs(x1-x0)+abs(y1-y0)
                graph[i] += [(j, dist)]
                graph[j] += [(i, dist)]
        res, visited, heap = 0, set(), [(0, 0)]
        while heap and len(visited) <= len(points):
            dist, node = heapq.heappop(heap)
            if node in visited:
                continue
            #print(dist, node, visited)
            res += dist
            visited.add(node)
            for (n, d) in graph[node]:
                if n in visited:
                    continue
                heapq.heappush(heap, (d, n))
        return res

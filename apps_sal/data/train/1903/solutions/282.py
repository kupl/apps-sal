import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = [[] for i in range(n)]
        for i in range(n - 1):
            for j in range(i + 1, n):
                md = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges[i].append((md, j))
                edges[j].append((md, i))
        i = 0
        visited = set()
        visited.add(i)
        li = edges[i]
        heapq.heapify(li)
        result = 0
        while li:
            d, j = heapq.heappop(li)
            if j not in visited:
                visited.add(j)
                result += d
                if len(visited) == n:
                    return result
                for edge in edges[j]:
                    if edge[1] not in visited:
                        heapq.heappush(li, edge)
        return result

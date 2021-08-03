

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        n = len(points)
        for i in range(n):
            for j in range(n):
                if i != j:
                    graph[i].append((abs(points[j][0] - points[i][0]) + abs(points[j][1] - points[i][1]), j))

        heap = [(0, 0)]
        res = 0
        visited = set()
        while heap:
            weight, dest = heapq.heappop(heap)
            if dest in visited:
                continue
            res += weight
            visited.add(dest)

            for cost, nei in graph[dest]:
                if nei not in visited:
                    heapq.heappush(heap, (cost, nei))

        return res

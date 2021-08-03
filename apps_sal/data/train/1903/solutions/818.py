import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        n = len(points)
        for i in range(n):
            for j in range(i):
                dis = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                graph[i].append((dis, j))
                graph[j].append((dis, i))

        visited = set()
        h = [(0, 0)]
        count = 0
        while h:
            dis, node = heapq.heappop(h)
            if node in visited:
                continue
            visited.add(node)
            count += dis
            for d, nxt in graph[node]:
                if nxt not in visited:
                    heapq.heappush(h, (d, nxt))
        return count

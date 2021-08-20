from heapq import heappush, heappop


class Solution:

    def manhattan(self, point1, point2):
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(points)
        for i in range(n):
            for j in range(n):
                if i != j:
                    graph[i].append([self.manhattan(points[i], points[j]), j])
        heap = [(0, 0)]
        visited = set()
        answer = 0
        while len(visited) < n:
            (distance, node) = heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            answer += distance
            for (weight, nei) in graph[node]:
                if nei not in visited:
                    heappush(heap, (weight, nei))
        return answer

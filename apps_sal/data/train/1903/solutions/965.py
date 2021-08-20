class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0
        visited = [0] * len(points)
        q = []
        start = 0
        for i in range(1, len(points)):
            dist = abs(points[i][0] - points[0][0]) + abs(points[i][1] - points[0][1])
            q.append([dist, i])
        heapq.heapify(q)
        visited[0] = 1
        cost = 0
        count = 1
        while True:
            x = heapq.heappop(q)
            if visited[x[1]] == 0:
                cost = cost + x[0]
                visited[x[1]] = 1
                count = count + 1
            if count == len(points):
                return cost
            for i in range(len(points)):
                if visited[i] == 0:
                    dist = abs(points[i][0] - points[x[1]][0]) + abs(points[i][1] - points[x[1]][1])
                    heapq.heappush(q, [dist, i])

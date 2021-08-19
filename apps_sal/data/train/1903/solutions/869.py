class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dis = {}
        length = len(points)
        for i in range(length):
            dis[i] = []
        res = 0
        for i in range(length):
            for j in range(length):
                if i == j:
                    continue
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heapq.heappush(dis[i], (d, j))
        visited = set([0])
        res = 0
        while len(visited) < length:
            curMin = -1
            for p in visited:
                while dis[p][0][1] in visited:
                    heapq.heappop(dis[p])
                if curMin == -1 or dis[p][0][0] < dis[curMin][0][0]:
                    curMin = p
            visited.add(dis[curMin][0][1])
            res += dis[curMin][0][0]
            heapq.heappop(dis[curMin])
        return res

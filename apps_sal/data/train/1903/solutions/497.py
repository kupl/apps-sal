from heapq import *


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dist = []
        for i in range(len(points)):
            dist.append([])
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                dist[i].append((d, i, j))
                dist[j].append((d, j, i))

        visited = [False] * len(points)
        hq = []
        for x in dist[0]:
            heappush(hq, x)
        visited[0] = True
        cost = 0
        print(hq)
        while not all(visited):
            d, i, j = heappop(hq)
            if visited[i] and visited[j]:
                continue

            if visited[i] == False:
                ind = i
            else:
                ind = j

            visited[ind] = True
            cost += d
            for x in dist[ind]:
                if visited[x[1]] == False or visited[x[2]] == False:
                    heappush(hq, x)
        return cost

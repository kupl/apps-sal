class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        graph = defaultdict(list)
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                cost = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                graph[i].append((cost, j))
                graph[j].append((cost, i))
        
        seen = [0] * (len(points)+1)
        seen[0] = 1
        q = graph[0]
        minimumCost = 0
        connectedNodes = 1
        heapq.heapify(q)
        while q:
            cost, point = heapq.heappop(q)
            if not seen[point]:
                seen[point] = 1
                minimumCost += cost
                connectedNodes += 1
                for connectingCost, neighbour in graph[point]:
                    heapq.heappush(q, (connectingCost, neighbour))
            if connectedNodes >= len(points):
                break
        return minimumCost

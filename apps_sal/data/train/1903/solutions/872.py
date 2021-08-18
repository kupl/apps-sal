class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        from queue import PriorityQueue

        coors = {}
        count = 0
        for point in points:
            coors[count] = tuple(point)
            count = count + 1
        pq = PriorityQueue()
        pq.put((0, 0))
        visited = set()
        total = 0
        while (len(visited) < len(points)):
            cost, nodeIdx = pq.get()
            if nodeIdx in visited:
                continue
            total = total + cost
            visited.add(nodeIdx)
            node = coors[nodeIdx]
            for nextNodeIdx in range(len(points)):
                if nextNodeIdx not in visited:
                    nextNode = coors[nextNodeIdx]
                    nextCost = abs(nextNode[0] - node[0]) + abs(nextNode[1] - node[1])
                    pq.put((nextCost, nextNodeIdx))
        return total

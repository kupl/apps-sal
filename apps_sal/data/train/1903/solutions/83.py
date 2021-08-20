class Solution:

    def calculateDistance(self, point1, point2):
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        queue = []
        queueSet = [0] * len(points)
        setDict = {}
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                heappush(queue, (self.calculateDistance(points[i], points[j]), points[i], points[j]))
            queueSet[i] = [tuple(points[i])]
            setDict[tuple(points[i])] = i
        totalCost = 0
        while queue:
            p = heappop(queue)
            t1 = tuple(p[1])
            t2 = tuple(p[2])
            if setDict[t1] != setDict[t2]:
                totalCost = totalCost + p[0]
                if setDict[t1] < setDict[t2]:
                    queueSet[setDict[t1]].extend(queueSet[setDict[t2]])
                    for ch in queueSet[setDict[t2]]:
                        setDict[ch] = setDict[t1]
                    setDict[t2] = setDict[t1]
                else:
                    queueSet[setDict[t2]].extend(queueSet[setDict[t1]])
                    for ch in queueSet[setDict[t1]]:
                        setDict[ch] = setDict[t2]
                    setDict[t1] = setDict[t2]
        return totalCost

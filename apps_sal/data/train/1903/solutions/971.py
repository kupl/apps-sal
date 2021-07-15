class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def getDistance(x1, y1, x2, y2):
            return abs(x1 - x2) + abs(y1 - y2)
        
        dist = defaultdict(list)
        for i in range(len(points)):
            curX, curY = points[i]
            d = []
            for j in range(len(points)):
                newX, newY = points[j]
                if newX == curX and newY == curY:
                    d.append((10 ** 20, j))
                else:
                    d.append((getDistance(curX, curY, newX, newY), j))
            # print(\"before\", d)
            heapq.heapify(d)
            # print(\"after\", d)
            dist[i] = d
        result = 0
        processed = set()
        processed.add(0)
        # print(dist)
        while len(processed) < len(points):
            possible = []
            for curNode in processed:
                curHeap = dist[curNode]
                while curHeap[0][1] in processed:
                    heapq.heappop(curHeap)
                possible.append(curHeap[0])
            index = -1
            minVal = float(\"inf\")
            for distance, ind in possible:
                if distance < minVal:
                    minVal = distance
                    index = ind
            processed.add(index)
            result += minVal
        return result
            
                
        
        
        
        
        
        
        
        
        
        # processed = set()
        # for i in range(len(points)):
        #     if len(processed) == 0:
        #         processed.add(i)
        #     else:
        #         curDistances = dist[i]
        #         for curDistance, index in curDistances:
        #             if index not in processed:
        #                 processed.add(index)
        #                 result += curDistance
        #                 print(curDistance)
        #                 break
        # return result

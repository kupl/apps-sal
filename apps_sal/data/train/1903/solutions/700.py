from heapq import heappush

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        minCost = 0
        minEdges = []
        # weight, idx 
        heappush(minEdges,(0,0))
             
        while(len(visited) < len(points)):  
            
            # pop to get the lowest weight edge possible
            # visit it and add cost to min cost spanning tree
            vertexDistance,vertexIdx = heappop(minEdges)
            if vertexIdx in visited: continue
            print(vertexIdx)
            visited.add(vertexIdx)
            minCost += vertexDistance
            
            # extract our currently visited x and y pos
            vertexX = points[vertexIdx][0]
            vertexY = points[vertexIdx][1]
            
            # for all nodes, if its not added to spanning tree already
            # calculate the distance to it. push it to heapq.
            for adjIdx, adjPos in enumerate(points):
                if adjIdx not in visited:
                    adjX = points[adjIdx][0]
                    adjY = points[adjIdx][1]
                    
                    distance = abs(vertexX - adjX) + abs(vertexY - adjY)
                    heappush(minEdges,(distance,adjIdx))
                             
        return minCost
                    
            
            
            


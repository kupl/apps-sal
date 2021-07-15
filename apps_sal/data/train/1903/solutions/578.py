from heapq import heappush,heappop
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def calcCost(i,j):
            return abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
        totalCost,visited,q=0,set(),[(0,0)]
        while len(visited)!=len(points):
            cost,point=heappop(q)
            if point not in visited:
                visited.add(point)
                totalCost+=cost
                for i in range(len(points)):
                    if i!=point:
                        heappush(q,(calcCost(point,i),i))
        return totalCost

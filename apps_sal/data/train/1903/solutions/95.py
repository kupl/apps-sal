from heapq import heappop, heappush, heapify 
from collections import defaultdict

def distance(pointA, pointB):
    
    return abs(pointA[0]-pointB[0]) + abs(pointA[1]-pointB[1])

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        n = len(points)
        
        mat = [[float('inf')] * n for i in range(n)]
        
        lookup = defaultdict(list)
        minHeap = []
        
        for idx, aPoint in enumerate(points):
            for bIdx in range(idx+1, n):
                bPoint = points[bIdx]
                
                dist = distance(aPoint, bPoint)
                
                minHeap.append(dist)
                
                lookup[dist].append([idx, bIdx])
                                
        if n == 1:
            return 0
        
        visited = set()
        cost = 0
        
        minHeap = sorted(minHeap)
        minValue = minHeap[0]
        minIndex = lookup[minValue][0]
        visited.add(minIndex[0])
        visited.add(minIndex[1])
        cost += minValue
        
        while len(visited) != n:
            for minValue in minHeap:
                minIndexs = lookup[minValue]
                ifFound = False
                                    
                for minIndex in minIndexs:
                    x = minIndex[0]
                    y = minIndex[1]
                    if x in visited and y in visited:
                        continue
                    elif x in visited or y in visited:
                        visited.add(x)
                        visited.add(y)
                        cost += minValue
                        ifFound = True
                        break
                if ifFound:
                    break
                
                        
        return cost
        
        
#         visited = set()
#         costs = []
#         minValue = float('inf')
#         minIndex = (0,0)
#         for i in range(n):
#             for j in range(n):
#                 if mat[i][j] < minValue:
#                     minValue = min(minValue, mat[i][j])
#                     minIndex = (i,j)
        
#         visited.add(minIndex[0])
#         visited.add(minIndex[1])
#         costs.append(minValue)
                
#         while len(visited) != n:
#             minValue = float('inf')
#             minIndex = (0,0)
#             for i in visited:
#                 for idx, value in enumerate(mat[i]):
#                     if value < minValue and idx not in visited:
#                         minValue = min(minValue, value)
#                         minIndex = (i, idx)
                                
#             visited.add(minIndex[0])
#             visited.add(minIndex[1])
#             costs.append(minValue)
#             mat[minIndex[0]][minIndex[1]] = float('inf')
#             mat[minIndex[1]][minIndex[0]] = float('inf')
         
#         return sum(costs)
        
            
        
        
        
        
            


'''
Idea is that we figure out for each city i all cities with index larger than i are reachable with distance at most distanceThreshold.
'''
import heapq
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        distances = defaultdict(dict)##will map for a vertex i to a dictionary containing key value pairs of the form j,distance, where distance from i to j is distance.
        edgeWeights = defaultdict(dict)
        for start,end,weight in edges:
            edgeWeights[start][end] = weight
            edgeWeights[end][start] = weight
        def computeDistances(i):##we will compute minimum distance for all vertices from i.
            iHeap = []
            heapq.heapify(iHeap)##remember you create list first and then heapify.
            heapq.heappush(iHeap,(0,i))
            visited = set()##need to ensure we don't go back and forth
            while iHeap:
                distance,vertex = heapq.heappop(iHeap)
                if vertex in visited:##don't want to expand a vertex if we already found its minimum distance
                    continue
                if distance > distanceThreshold:
                    break
                else:
                    distances[i][vertex] = distance##we know this vertex has to have closest distance to i
                    visited.add(vertex)##this is when we know we have found minimum distance
                    for neighbor in edgeWeights[vertex]:
                        if neighbor < i and i not in distances[neighbor]:##this means we already have that neighbor is not within a distance of i, so no chance. we can have neighbor appear in i.
                            continue
                        edgeWeight = edgeWeights[vertex][neighbor]
                        heapq.heappush(iHeap,(distance+edgeWeight,neighbor))
        lowestNumber = n
        lowestCity = -1
        for i in range(n):
            computeDistances(i)
            if len(distances[i]) <= lowestNumber:
                lowestNumber = len(distances[i])
                lowestCity = i
        ##print(distances)
        return lowestCity


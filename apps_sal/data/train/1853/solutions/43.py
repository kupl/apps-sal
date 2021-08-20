"""
Idea is that we figure out for each city i all cities with index larger than i are reachable with distance at most distanceThreshold.
"""
import heapq


class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        distances = defaultdict(dict)
        edgeWeights = defaultdict(dict)
        for (start, end, weight) in edges:
            edgeWeights[start][end] = weight
            edgeWeights[end][start] = weight

        def computeDistances(i):
            iHeap = []
            heapq.heapify(iHeap)
            heapq.heappush(iHeap, (0, i))
            visited = set()
            while iHeap:
                (distance, vertex) = heapq.heappop(iHeap)
                if vertex in visited:
                    continue
                if distance > distanceThreshold:
                    break
                else:
                    distances[i][vertex] = distance
                    visited.add(vertex)
                    for neighbor in edgeWeights[vertex]:
                        if neighbor < i and i not in distances[neighbor]:
                            continue
                        edgeWeight = edgeWeights[vertex][neighbor]
                        heapq.heappush(iHeap, (distance + edgeWeight, neighbor))
        lowestNumber = n
        lowestCity = -1
        for i in range(n):
            computeDistances(i)
            if len(distances[i]) <= lowestNumber:
                lowestNumber = len(distances[i])
                lowestCity = i
        return lowestCity

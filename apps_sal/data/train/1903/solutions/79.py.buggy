
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                dist = abs(points[j][1]-points[i][1]) + abs(points[j][0] - points[i][0])
                
                graph[i].append((j, dist))
                graph[j].append((i, dist))
        #print(graph)
        dist = {}
\t\t# Using heap to find min wt
        heap = [(0, 0)]
        while heap:
            ddist, node = heapq.heappop(heap)
            if node in dist:
                continue
            dist[node] = ddist
            for neighbor, d in graph[node]:
                if neighbor not in dist:
                    heapq.heappush (heap, (d, neighbor))
        return sum(dist.values())

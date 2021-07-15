
from collections import defaultdict
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = defaultdict(list)
        start = points[0]
\t\t
         
        #Storing the data in parent Directory
        dist = {}
        N = len(points)
\t\t# Using heap to find min wt
        heap = [(0, tuple(start))]
        while heap:
            ddist, node = heapq.heappop(heap)
            if node in dist:
                continue
            dist[node] = ddist
            for neighbor in points:
                if tuple(neighbor) not in dist:
                    d = abs(node[0]-neighbor[0]) + abs(node[1]-neighbor[1])
                    heapq.heappush (heap, (d, tuple(neighbor)))
            if len(dist) == N:
                break
        return sum(dist.values()) if len(dist) == N else -1

    
class Solution1:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        uf = {}

        # create union find for the initial edges given 
        def find(edge):
            uf.setdefault(edge, edge)
            if uf[edge] != edge:
                uf[edge] = find(uf[edge])
            return uf[edge]

        def union(edge1, edge2):
            uf[find(edge1)] = find(edge2)

       

        # sort the new edges by cost
        # if an edge is not part of the minimum spanning tree, then include it, else continue
        cost_ret = 0
        poss_mst = []
        for p1 in points:
            for p2 in points:
                dist = abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
                poss_mst.append([tuple(p1),tuple(p2),dist])
                
        for c1, c2, cost in sorted(poss_mst, key=lambda x : x[2]):
            if find(c1) != find(c2):
                union(c1, c2)
                cost_ret += cost

        return cost_ret
        

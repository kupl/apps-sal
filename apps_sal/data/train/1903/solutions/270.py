from queue import PriorityQueue

class Solution:
    def findParent(self, parents, i):
        if parents[i] is None:
            return i
        else:
            return self.findParent(parents, parents[i])
    
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        
        edges = []
        req_edges = len(points)-1
        dist = 0
        parents = [None] * len(points)
        ranks = [0] * len(points)
        
        for i, p1 in enumerate(points):
            for j, p2 in enumerate(points):
                if i < j:
                    edges.append([i, j, (abs(p1[0]-p2[0]) + abs(p1[1]-p2[1]))])
        edges = sorted(edges, key=lambda x: x[2])
        
        for edge in edges:
            parent_i = self.findParent(parents, edge[0])
            parent_j = self.findParent(parents, edge[1])
            if parent_i == parent_j:
                continue
            if ranks[parent_i] < ranks[parent_j]:
                parents[parent_i] = parent_j
            elif ranks[parent_i] > ranks[parent_j]:
                parents[parent_j] = parent_i
            else:
                parents[parent_i] = parent_j
                ranks[parent_j] += 1
            dist += edge[2]

            req_edges -= 1
            if req_edges == 0:
                break
            
        return dist


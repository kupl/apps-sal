import math
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = set()
        for i in range(n):
            p = points[i]
            for j in range(n):
                if i!=j:
                    w = abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                    e = (min(i,j),max(i,j),w)
                    edges.add(e)
        edges = sorted(edges, key = lambda x: x[2])
        tree_id = [0]*n
        for i in range(n):
            tree_id[i] = i
        cost = 0
        for i in edges:
            v1 = i[0]
            v2 = i[1]
            w = i[2]
            if tree_id[v1] != tree_id[v2]:
                cost += w
                old_tree = tree_id[v1]
                new_tree = tree_id[v2]
                for j in range(n):
                    if tree_id[j] == old_tree:
                        tree_id[j] = new_tree
        return cost
            
        
        
        
                    


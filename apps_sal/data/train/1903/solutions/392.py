def manhattan(p1, p2):
    if p1 == p2:
        return 10**10
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
def makeGraph(points):
    graph = []
    for p1 in range(len(points)):
        for p2 in range(p1):
            graph.append( (p2, p1, manhattan(points[p1], points[p2])) )
    return graph

class Solution:

    #Prim's
    def _minCostConnectPoints(self, points: List[List[int]]) -> int:
        pass
        
        
        
        
    #Kruskal's
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        
        
        def find(subsets, p1):
            if subsets[p1][0] != p1:
                subsets[p1][0] = find(subsets, subsets[p1][0])
            return subsets[p1][0]
        
        def union(subsets, p1, p2):
            p1root = find(subsets, p1)
            p2root = find(subsets, p2)
            
            if subsets[p1root][1] > subsets[p2root][1]:
                subsets[p2root][0] = p1root
            elif subsets[p2root][1] > subsets[p1root][1]:
                subsets[p1root][0] = p2root
            else:
                subsets[p1root][1] += 1
                subsets[p2root][0] = p1root
        
        graph = makeGraph(points)
        
        edges = sorted(graph, key=lambda x: x[2])
        subsets = [[x, 0] for x in range(len(points))]
        
        e = 0 #counts how many edges have been added
        i = 0 #tracks location in edges array
        total_cost = 0
        
        while e < len(points) - 1:
            
            p1, p2, cost = edges[i]
            
            if find(subsets, p1) != find(subsets, p2):               
                union(subsets, p1, p2)
                total_cost += cost
                e += 1
            else:
                pass
                #discard the edge
            
            i += 1
        return total_cost

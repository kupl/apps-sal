class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # edge: from, to, weight
        Edge = namedtuple(\"Edge\", [\"V1\", \"V2\", \"dist\"])
        edges = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                edges.append(Edge(points[i], points[j], abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])))
        edges.sort(key = lambda e: e[2])
        
        uf = {}
        
        def find(x:List[int]):
            xx = (x[0], x[1]) # to a hashable type
            uf.setdefault(xx, xx) # this will only be executed when x's value is missing
            if uf[xx] != xx:
                uf[xx] = find(uf[xx])
            return uf[xx]
        
        def union(x, y):
            uf[find(x)] = find(y)
            
        num = len(points) # we need num-1 lines to form the MST
        
        count, total = 0, 0
        
        for f, t, dist in edges: # already sorted
            # when vertice x and vertice y doesn't have the same root, we union them 
            # and draw a line (count + 1)
            if find(f) != find(t):
                union(f, t)
                count += 1
                total += dist
            if count == num - 1:
                return total
        return total

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) < 2:
            return 0
        
        def dist(p1, p2):
            return abs(points[p1][0] - points[p2][0]) + abs(points[p1][1] - points[p2][1])
        
        edges = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                edges.append((i,j,dist(i, j)))
        edges = sorted(edges, key=lambda x : x[2])
        #print(edges)
        
        total = 0
        group = [x for x in range(len(points))]
        while sum(group) > 0:
            x, y, w = edges.pop(0)
            #print(group)
            #print(f\"{x} {y} {w} {total} {edges}\")
            if group[x] == group[y]:
                continue
            
            gx = group[x]
            gy = group[y]
            g = min(gx, gy)
            for i in range(len(group)):
                if group[i] == gy or group[i] == gx:
                    group[i] = g
                #print(f\"\\t{g} {i} {group}\")
            total += w
        #print(group)
        #print(f\"{x} {y} {w} {total} {edges}\")            
        return total


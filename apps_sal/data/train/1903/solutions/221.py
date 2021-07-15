class Solution(object):
    def minCostConnectPoints(self, points):
        \"\"\"
        :type points: List[List[int]]
        :rtype: int
        \"\"\"
        n = len(points)
        colors = list(range(n))
        sets = [[i] for i in range(n)]
        
        edges = []
        for i in range(n):
            for j in range(i):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((i, j, dist))
                
        edges.sort(key=lambda x: x[2])
        
        cost = 0
        for (x, y, d) in edges:
            if colors[x] == colors[y]:
                continue

            cost += d
            if len(sets[colors[x]]) < len(sets[colors[y]]):
                x, y = y, x

            #add y to x
            color_x = colors[x]
            color_y = colors[y]

            for node in sets[color_y]:
                colors[node] = color_x

            sets[color_x].extend(sets[color_y])

        return cost
        

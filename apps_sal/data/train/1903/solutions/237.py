class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        manhattan = lambda p1, p2: abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        
        ans, n = 0, len(points)
        seen = set()
        vertices = [(0, (0, 0))] # [(dist, ( , index)]
        # first zero is distance, middle zero is dummy value, last zero is next vertice. 
        # so ai point (0, 0) the heap will add the edges[0], and ans += 0.

        while len(seen) < n:
            w, (u, v) = heapq.heappop(vertices)            
            if v in seen: continue
            ans += w
            seen.add(v)
            for j in range(n):
                if j not in seen and j!=v:
                    heapq.heappush(vertices, (manhattan(points[j], points[v]), (v, j)))    
        return ans
    \"\"\"
            # select random start point
        # find the node that 1) search all possible route costs least 2) not generate a loop 3) among the ones that are not selected 
        if len(points) <= 1: return 0
        visited = [(points[0][0], points[0][1])]
        mustgo = points[1:]
        cost = 0
        while mustgo:
            route = dict()
            for p in visited:
                for m in mustgo:
                    if (m[0], m[1]) in route.keys():
                        route[(m[0], m[1])] = min(abs(p[0] - m[0]) + abs(p[1] - m[1]), route[(m[0], m[1])])
                    else:
                        route[(m[0], m[1])] = abs(p[0] - m[0]) + abs(p[1] - m[1])
            for k, v in route.items():
                if v == min(route.values()):
                    cost += v                    
                    visited.append(k)
                    mustgo.remove([k[0],k[1]])
        print((visited))
        return cost
    \"\"\"

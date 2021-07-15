class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # create MST over a created graph
        # G = collections.defaultdict(list)
        q = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                dis = abs(points[i][0]-points[j][0]) + abs(points[i][1] - points[j][1])
                q.append((dis, i, j))
                # G[i].append((dis,j))  # can sort based on dis
        
        # MST search algorithm: Prim and Kruskal
        # Kruskal
        # path compression
        def find(x):
            if (x != parent[x]):
                parent[x] = find(parent[x])
            return parent[x]
        # union by rank
        def union(x, y):
            if size[x] > size[y]:
                size[x] += size[y]
                parent[y] = x
            else:
                size[y] += size[x]
                parent[x] = y
                
        n = len(points)
        parent = [i for i in range(n+1)]
        size = [1 for _ in range(n+1)]  
        q.sort()  # sort edges
        res = 0
        count = 0
        for w, u, v in q:
            rA, rB = find(u), find(v)
            if rA == rB:
                continue
            union(rA, rB)
            res += w
            # Optimize so that we don't traverse all edges
            count += 1
            if count == n:
                return res
        return res 

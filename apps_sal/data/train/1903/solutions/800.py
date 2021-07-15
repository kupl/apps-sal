class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        nodes, edges = defaultdict(int), []
        
        def dis(i, j):
            x1, y1 = points[i][0], points[i][1]
            x2, y2 = points[j][0], points[j][1]
            return abs(x1-x2) + abs(y1-y2)
        
        n = len(points)
        for i in range(n):
            for j in range(i+1, n):
                edges.append((i, j, dis(i, j)))
                
                
        edges.sort(key=lambda x: x[2])
        # print(edges)
        
        fa = defaultdict(lambda: -1)
        def find(i):
            if fa[i] == -1 or i == fa[i]: return i
            fa[i] = find(fa[i])
            return fa[i]
        
        ans = 0
        for i, j, c in edges:
            fi = find(i)
            fj = find(j)
            if fi == fj: continue
            ans += c
            fa[fi] = fj
            
        return ans

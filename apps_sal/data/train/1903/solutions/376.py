class Solution:
    def find_min_node(self, n, key, mst_set):
        min, min_node = sys.maxsize, -1
        for i in range(n):
            if not mst_set[i] and key[i] < min:
                min, min_node = key[i], i
        return min_node
    
    def solve(self, n, edges):
        mst_set = [False] * n;
        key = [sys.maxsize] * n;
        parent = [-1] * n;
        
        key[0] = 0
        parent[0] = -1
        
        for i in range(n):
            u = self.find_min_node(n, key, mst_set)
            mst_set[u] = True
            for v in range(n):
                if (not mst_set[v] and edges[u][v] < key[v]):
                    parent[v] = u
                    key[v] = edges[u][v]
        
        res = 0
        for i in range(1, n):
            res += edges[parent[i]][i]
        return res
        
        
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                edges[i][j] = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                
        return self.solve(n, edges)


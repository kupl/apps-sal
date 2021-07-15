class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n + 1))
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x]) 
            return parent[x]
        
        def union(x , y):
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[rx] = ry
                return 1
            else:
                return 0
        
        res, e1, e2 = 0, 0, 0
        
        for t, i, j in edges:
            if t == 3:
                if union(i, j):
                    e1 += 1
                    e2 += 1
                else:
                    res += 1
                    
        parent1 = parent[:]
        
        for t, i ,j in edges:
            if t == 1:
                if union(i, j):
                    e1 += 1
                else:
                    res += 1
        
        parent = parent1
        for t, i, j in edges:
            if t == 2:
                if union(i, j):
                    e2 += 1
                else:
                    res += 1
        return res if e1 == e2 == n - 1 else -1
        


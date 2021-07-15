class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        def find(i):
            if parent[i] != i: parent[i] = find(parent[i])
            return parent[i]
            
        def union(x, y):
            x, y = find(x), find(y)
            if x == y: return True
            parent[x] = y
            return False
        
        res = a = b = 0
        parent = list(range(n+1))
        
        for t, u, v in edges:
            if t == 3:
                if union(u, v):
                    res += 1
                else:
                    a += 1
                    b += 1
                
        p1 = parent[:]
        for t, u, v in edges:
            if t == 1:
                if union(u, v):
                    res += 1
                else:
                    a += 1
        
        parent = p1
        for t, u, v in edges:
            if t == 2:
                if union(u, v):
                    res += 1
                else:
                    b += 1
                        
        return res if a == b == n-1 else -1

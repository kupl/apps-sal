class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        d = [{}, {}]
        
        def find(x, n):
            if x not in d[n]:
                d[n][x] = x
                return d[n][x]
            else:
                if d[n][x] != x:
                    d[n][x] = find(d[n][x], n)
                return d[n][x]
        
        def union(x, y, n):
            d[n][find(x, n)] = find(y, n)
            
        ans = 0
        edges.sort(reverse = True)
        for typeN, a, b in edges:
            if typeN == 3:
                if find(a, 0) == find(b, 0) and find(a, 1) == find(b, 1):
                    ans += 1
                else:
                    union(a, b, 0)
                    union(a, b, 1)
            else:
                if find(a, typeN-1) == find(b, typeN-1):
                    ans += 1
                else:
                    union(a, b, typeN-1)                    
        return -1 if any((find(1, 0) != find(i, 0) or find(1, 1) != find(i, 1)) for i in range(2, n+1)) else ans
                    
                    
                    
                    


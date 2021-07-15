class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # Union find
        def find(i):
            if i != root[i]:
                root[i] = find(root[i])
            return root[i]

        def uni(x, y):
            x, y = find(x), find(y)
            if x == y: 
                return False
            root[x] = y
            return True

        res = e1 = e2 = 0
        
        
        root = list(range(n+1))
        
        print(root)

        
        for typ, u, v in edges:
            if typ == 3:
                if uni(u, v):
                    e1 += 1
                    e2 += 1
                else:
                    res += 1
                    
        root_copy = root.copy()
        
        for typ, u, v in edges:
            if typ == 1:
                if uni(u, v):
                    e1 += 1
                else:
                    res += 1

        root = root_copy
        
        for typ, u, v in edges:
            if typ == 2:
                if uni(u, v):
                    e2 += 1
                else:
                    res += 1
                    
        return res if e1 == e2 == n - 1 else -1

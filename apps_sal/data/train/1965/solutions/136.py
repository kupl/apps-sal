class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        roots1 = [i for i in range(n + 1)]
        roots2 = [i for i in range(n + 1)]
        
        def find_root(roots, i):
            while roots[i] != i:
                roots[i] = roots[roots[i]]
                i = roots[i]
            return i
        
        ans = 0
        
        edges.sort(reverse=True)
        
        for edge in edges:
            if edge[0] == 3:
                if find_root(roots1, edge[1]) == find_root(roots1, edge[2]) and find_root(roots2, edge[1]) == find_root(roots2, edge[2]):
                    ans += 1
                else:
                    roots1[find_root(roots1, edge[2])] = find_root(roots1, edge[1])
                    roots2[find_root(roots2, edge[2])] = find_root(roots2, edge[1])
            elif edge[0] == 1:
                if find_root(roots1, edge[1]) == find_root(roots1, edge[2]):
                    ans += 1
                else:
                    roots1[find_root(roots1, edge[2])] = find_root(roots1, edge[1])
            else:
                if find_root(roots2, edge[1]) == find_root(roots2, edge[2]):
                    ans += 1
                else:
                    roots2[find_root(roots2, edge[2])] = find_root(roots2, edge[1])
        
        def check(roots):
            g = set()
            for i in range(1, len(roots)):
                g.add(find_root(roots, i))
            return 0 if len(g) > 1 else 1
        
        return -1 if not check(roots1) or not check(roots2) else ans
                    
        
        


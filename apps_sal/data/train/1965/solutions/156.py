import copy

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        parA, parB = [i for i in range(n + 1)], [i for i in range(n + 1)]
        cnta, cntb = n, n
        edges3 = [edge for edge in edges if edge[0] == 3]
        edges2 = [edge for edge in edges if edge[0] == 2]
        edges1 = [edge for edge in edges if edge[0] == 1]
        
        def find(par, x):
            p = par[x]
            while p != par[p]:
                p = par[p]
            par[x] = p
            return p

        ans = 0
        
        for e in edges3:
            x, y = find(parA, e[1]), find(parA, e[2])
            if x != y:
                parA[y] = x
                parB[y] = x
                cnta -= 1
                cntb -= 1
            else:
                ans += 1
        
        for e in edges1:
            x, y = find(parA, e[1]), find(parA, e[2])
            if x != y:
                parA[y] = x
                cnta -= 1
            else:
                ans += 1
                
        for e in edges2:
            x, y = find(parB, e[1]), find(parB, e[2])
            if x != y:
                parB[y] = parB[x]
                cntb -= 1
            else:
                ans += 1
        if cnta != 1 or cntb != 1:
            return -1
        
        return ans

    


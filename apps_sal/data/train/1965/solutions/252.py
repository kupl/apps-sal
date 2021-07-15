class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        m = len(edges)
        
        g1 = [set() for i in range(n)]
        g2 = [set() for i in range(n)]
        g = [[] for i in range(n)]
        for t, u, v in edges:
            u -= 1
            v -= 1
            if t != 1:
                g2[u].add(v)
                g2[v].add(u)
                
            if t != 2:
                g1[u].add(v)
                g1[v].add(u)
                
            if t == 3:
                g[u].append(v)
                g[v].append(u)
                
        vs = [False] * n
        stk = [0]
        
        while stk:
            idx = stk.pop()
            vs[idx] = True
            
            for ne in g1[idx]:
                if not vs[ne]:
                    stk.append(ne)
        
        for i in range(n):
            if not vs[i]:
                return -1
        
        
        vs = [False] * n
        stk = [0]
        
        while stk:
            idx = stk.pop()
            vs[idx] = True
            
            for ne in g2[idx]:
                if not vs[ne]:
                    stk.append(ne)
        
        
        for i in range(n):
            if not vs[i]:
                return -1
        
        vs = [False] * n
        color = 0
        count = 0
        for i in range(n):
            if not vs[i]:
                color += 1
                tc = 0
                stk = [i]
                while stk:
                    idx = stk.pop()
                    if not vs[idx]:
                        vs[idx] = True
                        tc += 1
                    
                    for ne in g[idx]:
                        if not vs[ne]:
                            stk.append(ne)
                            
                count += tc - 1
                
        print(count)
        print(color)
        
        return m - (count + (color * 2 - 2))
                    


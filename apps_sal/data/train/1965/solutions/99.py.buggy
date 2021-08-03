class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        def root(i):
            while par[i] != i:
                par[i] = par[par[i]]
                i = par[i]
            return i
        
        def connected(i, j):
            x = root(i)
            y = root(j)
            return x == y
        
        def union(i, j):
            x = root(i)
            y = root(j)
            if x == y:
                return
            if sz[x] <= sz[y]:
                par[x] =  y
                sz[y] += sz[x]
            else:
                par[y] = x
                sz[x] += sz[y]
                
        par = {}
        sz  = {}
        st = set()
        edges.sort(key = lambda x : 0 - x[0])
        count = 0
        for e in edges:
            t = e[0]
            x = e[1]
            y = e[2]
            st.add(x)
            st.add(y)
            
            xa = str(e[1]) + \"a\"
            xb = str(e[1]) + \"b\"
            
            ya = str(e[2]) + \"a\"
            yb = str(e[2]) + \"b\"
            
            if xa not in par:
                par[xa] = xa
                sz[xa] = 1
            if xb not in par:
                par[xb] = xb
                sz[xb] = 1
                
            if ya not in par:
                par[ya] = ya
                sz[ya] = 1
                
            if yb not in par:
                par[yb] = yb
                sz[yb] = 1
                
            if t == 3:
                if connected(xa, ya) and connected(xb, yb):
                    count += 1
                    continue
                union(xa, ya)
                union(xb, yb)
            elif t == 2:
                if connected(xb, yb):
                    count += 1
                    continue
                union(xb, yb)
            else:
                if connected(xa, ya):
                    count += 1
                    continue
                union(xa, ya)
        
        mxa = 0
        mxb = 0
        for x in sz:
            if x[-1] == \"a\":
                mxa = max(mxa, sz[x])
            elif x[-1] == \"b\":
                mxb = max(mxb, sz[x])
                
        if mxa == len(st) and mxb == len(st):
            return count
        return -1
            
                
                
                
                    
                
                
        
        

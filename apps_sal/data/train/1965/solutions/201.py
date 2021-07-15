class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        dtype = collections.defaultdict(set)
        
        for e in edges:
            dtype[(e[1], e[2])].add(e[0])
        
        res = 0
        
        for k in dtype:
            if 3 in dtype[k]:
                if 1 in dtype[k]:
                    res += 1
                    dtype[k].remove(1)
                if 2 in dtype[k]:
                    res += 1
                    dtype[k].remove(2)
        
        da = collections.defaultdict(set)
        db = collections.defaultdict(set)
        
        for k in dtype:
            if (1 in dtype[k]) or (3 in dtype[k]):
                da[k[0]].add(k[1])
                da[k[1]].add(k[0])
            if (2 in dtype[k]) or (3 in dtype[k]):
                db[k[0]].add(k[1])
                db[k[1]].add(k[0])
        
        def traversable(dd):
            q = collections.deque([1])
            v = set([1])
            
            while q:
                node = q.popleft()
                for nei in dd[node]:
                    if (nei not in v):
                        q.append(nei)
                        v.add(nei)
            if len(v) != n:
                return False
            return True
                        
        
        if (not traversable(da)) or (not traversable(db)):
            return -1
        
        
        d3 = collections.defaultdict(set)
        
        for k in dtype:
            if (3 in dtype[k]):
                d3[k[0]].add(k[1])
                d3[k[1]].add(k[0])
        
        def components(dd):
            r = []
            
            v = set()
            nodes = list(dd.keys())
            lastvsize = 0
            for node in nodes:
                if node not in v:
                    v.add(node)
                    q = collections.deque([node])
                    
                    while q:
                        node = q.popleft()
                        for nei in dd[node]:
                            if (nei not in v):
                                q.append(nei)
                                v.add(nei)
                    r.append(len(v) - lastvsize)
                    lastvsize = len(v)
            return r
        
        d3ComponentSizes = components(d3)
        need3 = 0
        for compSize in d3ComponentSizes:
            need3 += compSize - 1 
        d3nodes = len(list(d3.keys()))
        need1 = len(d3ComponentSizes) - 1 + n - d3nodes
        need2 = len(d3ComponentSizes) - 1 + n - d3nodes
        print(d3ComponentSizes)
        print((len(edges), need1, need2, need3))
        return len(edges) - (need1 + need2 + need3)


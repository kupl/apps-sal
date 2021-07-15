class Solution:
    def maxNumEdgesToRemove(self, n: int, edges) -> int:
        N = len(edges)
        dup = set()
        res = 0
        c1, c2, bc = 0, 0, 0
        alice, bob, both = defaultdict(list), defaultdict(list), defaultdict(list)
        
        for t, u, v in edges:
            if (t, u, v) not in dup:
                dup.add((t, u, v))
                if t == 1 or t == 3:
                    if t == 1:
                        c1 += 1
                    alice[u].append(v)
                    alice[v].append(u)
                if t == 2 or t == 3:
                    if t == 2:
                        c2 += 1
                    bob[u].append(v)
                    bob[v].append(u)
                if t == 3:
                    bc += 1
                    both[u].append(v)
                    both[v].append(u)
            else:
                res += 1
        # print(res)
        
        va, vb, = set(), set()
        vc = dict()
        
        def dfs(node, t):
            if t == 1:
                va.add(node)
                for ngb in alice[node]:
                    if not ngb in va:
                        dfs(ngb, t)
            else:
                vb.add(node)
                for ngb in bob[node]:
                    if not ngb in vb:
                        dfs(ngb, t)
        
        dfs(1, 1)
        dfs(1, 2)
        
        if len(va) < n or len(vb) < n:
            return -1
        
        def dfs_both(node, prev, idx):
            vc[node] = idx
            for ngb in both[node]:
                if ngb == prev:
                    continue
                if ngb not in vc:
                    dfs_both(ngb, node, idx)
                
        idx = 0
        for i in both:
            if i not in vc:
                idx += 1
                dfs_both(i, -1, idx)
            
        bc_need = 0
        for i in range(1, idx + 1):
            cluster = 0
            for node in vc:
                if vc[node] == i:
                    cluster += 1
            bc_need += cluster - 1
                
        res += bc - bc_need
        # print(bc)
        # print(c1)
        # print(c2)
        # print(res)
        # print(bc_need)
        
        res += c1 - (n - 1 - bc_need)
        res += c2 - (n - 1 - bc_need)
        return res

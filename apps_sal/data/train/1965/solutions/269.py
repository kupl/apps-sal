class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        f = {}
        t = {}
        ans = 0
        def ffind(a):
            f.setdefault(a,a)
            if f[a] != a:
                f[a] = ffind(f[a])
            return f[a]
        def funion(a,b):
            f.setdefault(a,a)
            f.setdefault(b,b)
            if ffind(a) == ffind(b): return False
            f[ffind(a)] = f[ffind(b)]
            return True
        def tfind(a):
            t.setdefault(a,a)
            if t[a] != a:
                t[a] = tfind(t[a])
            return t[a]
        def tunion(a,b):
            t.setdefault(a,a)
            t.setdefault(b,b)
            if tfind(a) == tfind(b): return False
            t[tfind(a)] = t[tfind(b)]
            return True
        
        for ty, a, b in edges:
            if ty!= 3: continue
            tunion(a,b)
            if not funion(a,b):
                ans += 1
        for ty, a, b in edges:
            if ty!=1: continue
            if not funion(a,b):
                ans += 1
        for ty, a, b in edges:
            if ty!=2: continue
            if not tunion(a,b):
                ans += 1
        if len(f) != n or len(t) != n: return -1
        return ans
        
        


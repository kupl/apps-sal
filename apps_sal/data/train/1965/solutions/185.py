class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        def find(x, p):
            if p[x] != x:
                p[x] = find(p[x], p)
            return p[x]
        
        def merge(rx, ry, p):
            p[rx] = ry
        
        res = 0
        pa = [i for i in range(n)]
        pb = [i for i in range(n)]
        
        edges.sort(key=lambda x: -x[0])
        
        for type_, u, v in edges:
            if type_ == 1:
                ru, rv = find(u - 1, pa), find(v - 1, pa)
                if ru == rv:
                    res += 1
                else:
                    merge(ru, rv, pa)
            elif type_ == 2:    
                ru, rv = find(u - 1, pb), find(v - 1, pb)
                if ru == rv:
                    res += 1
                else:
                    merge(ru, rv, pb)
            
            if type_ == 3:
                rua, rva = find(u - 1, pa), find(v - 1, pa)
                rub, rvb = find(u - 1, pb), find(v - 1, pb)
                if rua == rva and rub == rvb:
                    res += 1
                else:
                    merge(rua, rva, pa)
                    merge(rub, rvb, pb)
                    
        
        return res if len({find(i, pa) for i in range(n)}) == len({find(i, pb) for i in range(n)}) == 1 else -1


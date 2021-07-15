class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        hx = dict()
        hy = dict()
        
        for i, (x, y) in enumerate(points):
            hx.setdefault(x, set())
            hy.setdefault(y, set())
            
            hx[x].add(y)
            hy[y].add(x)
        
        res = float(\"inf\")
        
        
        for xa, ys in hy.items():
            for ya in ys:
                for xb in hx[ya]:
                    if xa < xb:
                        for yb in ys:
                            if yb < ya and yb in hy[xb]:
                                res = min(res, abs(xa - xb) * abs(ya - yb))
            
        return res if res < float(\"inf\") else 0
            

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        xd = collections.defaultdict(set)
        
        for p in points:
            xd[p[0]].add(p[1])
        
        yd = collections.defaultdict(list)
        
        for x, v in list(xd.items()):
            if len(v) < 2:
                continue
                
            ys = list(v)
            
            for i in range(len(ys)):
                for j in range(i+1, len(ys)):
                    miny, maxy = min(ys[i], ys[j]), max(ys[i], ys[j])
                    yd[(miny, maxy)].append(x)
                    
        res = float('inf')
        
        for ypair, xlist in list(yd.items()):
            if len(xlist) < 2:
                continue
            
            xlist = sorted(xlist)
            h = ypair[1] - ypair[0]
            
            for i in range(len(xlist)-1):
                res = min(res, h * (xlist[i+1] - xlist[i]))
        
        return res if res != float('inf') else 0
                
            
             
            
        


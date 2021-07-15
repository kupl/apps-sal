class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        dictY=collections.defaultdict(list)
        for i, (x, y) in enumerate(points):
            dictY[y].append(i)
        
        y2Xpair=collections.defaultdict(set)
        for y in dictY.keys():
            if len(dictY[y])<=1:
                continue
                
            for p1, p2 in itertools.combinations(dictY[y], 2):
                x1, _, x2, _ = points[p1] + points[p2]
                y2Xpair[y].add((min(x1,x2), max(x1,x2)))  
            
        res=float('inf')
        for (y1,p1), (y2, p2) in itertools.combinations(y2Xpair.items(), 2):
            h=abs(y1-y2)
            for x1, x2 in p1&p2:
                res=min(res, (x2-x1)*h)
        
             
        return 0 if res==float('inf') else res

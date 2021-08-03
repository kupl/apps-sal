class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        \"\"\"
        | x   x x
        |   x x x
        | x   x    x1:y1,y3
        |________  x2:y2
                   x3:y1,y2,y3
                   x4:y2,y3
        \"\"\"
        minarea=float('inf')
        d = defaultdict(set)
        for x,y in points:
            d[x].add(y)
        sortx=sorted(d)
        
        #print(d)
        for i in range(len(sortx)):
            for j in range(i+1, len(sortx)):
                ys= d[sortx[i]] & d[sortx[j]]
                if len(ys)>1:
                    ylist = list(ys)
                    ylist.sort()
                    ylen =min([abs(ii-jj) for ii, jj in zip(ylist, ylist[1:])])
                    
                    minarea = min(minarea, abs(sortx[i]-sortx[j])*ylen)
                
        return minarea if minarea!=float('inf') else 0

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        xMap = defaultdict(set)
        yMap = defaultdict(int)
        
        for x,y in points:
            yMap[y] += 1
            xMap[x].add(y)
        
        
        
        xUnique = list(xMap.keys())
        xUnique.sort()
        
        res = float(\"inf\")
        for i in range(len(xUnique)):
            for j in range(i+1, len(xUnique)):
                x1 = xUnique[i]
                x2 = xUnique[j]
                
                values = xMap[x1].intersection(xMap[x2])
                
                values = list(sorted(values))
            
                minDiff = float(\"inf\")
                for k in range(1, len(values)):
                    minDiff = min(minDiff, values[k] - values[k-1])
                
                if minDiff == float(\"inf\"):
                    continue
                
                res = min(res, (x2 - x1) * minDiff)
        
        if res == float(\"inf\"):
            return 0
        
        return res
                
                
        
        
        

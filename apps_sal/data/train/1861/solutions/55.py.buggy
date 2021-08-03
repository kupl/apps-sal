class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        x_dict = defaultdict(set)
        for p in points:
            x_dict[p[0]].add(p[1])

        min_area = float(\"inf\")
        x = sorted(list(x_dict.keys()))
        for i in range(len(x)):
            for j in range(i+1, len(x)):
                y = sorted(list(x_dict[x[i]] & x_dict[x[j]]))
                if len(y)>1:
                    min_height = min(y[k]-y[k-1] for k in range(1, len(y)))
                    min_area = min(min_area, (x[j]-x[i])*min_height)
        
        if min_area == float(\"inf\"):
            return 0
        
        return min_area
    
                    
                
                

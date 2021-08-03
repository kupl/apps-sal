class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        
        cols = collections.defaultdict(list)
        
        for x, y in points:
            cols[x].append(y)
        
        min_ = float(\"inf\")
        pre_x = {}
        
        for x2 in sorted(cols):
            cols[x2] = sorted(cols[x2])
            for j in range(len(cols[x2])):
                for i in range(j):
                    y1 = cols[x2][i]
                    y2 = cols[x2][j]
                    if (y1,y2) in pre_x:
                        delta_x = x2 - pre_x[y1,y2]
                        delta_y = y2 - y1
                        area =  delta_x * delta_y
                        min_ = min(min_, area)
                    
                    pre_x[y1,y2] = x2
        
        return min_ if min_ < float(\"inf\") else 0
                        
                        

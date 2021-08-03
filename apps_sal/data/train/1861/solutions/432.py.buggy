from collections import defaultdict

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        result = float(\"inf\")
        found = False
        
        point_by_x = defaultdict(set)
        
        for x, y in points:
            point_by_x[x].add(y)
            
        y_pair_to_x = dict()
        sorted_x = sorted(list(point_by_x.keys()))

        for x in sorted_x:
            y_list = sorted(list(point_by_x[x]))
            
            for i in range(len(y_list)):
                for j in range(i+1, len(y_list)):
                    v1, v2 = y_list[i], y_list[j]
                    if (v1, v2) in y_pair_to_x:
                        width = v2 - v1
                        height = x - y_pair_to_x[(v1, v2)]
                        result = min(result, width * height)
                        found = True
                    y_pair_to_x[(v1, v2)] = x
                    
        if not found:
            return 0
        return result
                    
        
        
        

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        \"\"\"
        Time complexity: O(n^2)
        Space complexity: O(n)
        \"\"\"
        # idea, use lookup set to store the point that has been seen before. for (x1,y1) in points, for (x2,y2) in lookup, check whether (x1,y2) and (x2, y1) in lookup. 
        
        min_area = float('inf') 
        lookup = set()
        
        
        for x1, y1 in points:
            for x2, y2 in lookup:
                if (x1, y2) in lookup and (x2, y1) in lookup:
                    min_area = min(min_area, abs(x1-x2) * abs(y1-y2)) 
                    
            # add to lookup for the outer loop
            lookup.add((x1, y1))
            
            
        if min_area != float('inf'):
            return min_area
        else:
            return 0

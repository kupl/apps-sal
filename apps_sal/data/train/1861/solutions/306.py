class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        # you need 4 points to make a rectangle
        # first dedupe and add elements to a set
        # for every x,y - iterate the remaining elements, idenitfy the new x,y is greater than current x,y
        # also check if there is x1,y2 and x2,y1 is present in the set:
        # then find the area, and process the minimum area
        
        pointset = set()
        minarea = float('inf')
        
        for x, y in points:
            pointset.add((x,y))
            
        
        for x1,y1 in pointset:
            for x2, y2 in pointset:
                if x1>x2 and y1>y2 and (x1,y2) in pointset and (x2,y1) in pointset:
                    area = abs(x1-x2) * abs(y1-y2)
                    minarea = min(area, minarea)
            
        if minarea == float('inf'):
            return 0
        else:
            return minarea
                        
                        
            
                        
                        
                    
                    
        
        
        
        


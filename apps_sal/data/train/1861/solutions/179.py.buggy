from collections import defaultdict
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
      
        
#   Assume one point(x1,y1) as bottom left and other (x2,y2) as top right point of a diagnol now search for   
        points=set([(i[0],i[1]) for i in points ])
        
        mini=float(\"INF\")
        # points.sort(key=lambda x:x[0])
        for point1 in points:
            for point2 in points: 
                x1,y1=point1
                x2,y2=point2
                
                if (x2>x1) and (y2>y1) and (x1,y2) in points and (x2,y1) in points:
                    # print(x1,y1,x2,y2)
                    mini=min(mini,(y2-y1)*(x2-x1)) 
            
        return mini if not mini==float(\"INF\") else 0
                
        
        

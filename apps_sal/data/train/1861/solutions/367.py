class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        
        st = set()
        
        min_area = float('inf')
        
        for item in points:
            st.add((item[0], item[1]))
            
        for i in range(len(points)-1):
            for j in range(i+1,len(points)):
                x1,y1 = points[i][0], points[i][1]
                
                x2,y2 = points[j][0], points[j][1]
                
                if x1 == x2 or y1 ==y2:
                    continue
                
                if (x1,y2) in st and (x2, y1) in st:
                    curr_area = abs((y2-y1) * (x2-x1))
                    min_area = min(min_area, curr_area)
        
        if min_area == float('inf'):
            return 0
        
        return min_area

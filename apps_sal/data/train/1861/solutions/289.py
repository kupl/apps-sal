# store column values for every x in a dictionary, find diagonal points
# time - O(n*n), space - O(n)


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        
        columns = defaultdict(set)
        minArea = float(\"inf\")
        
        for pt in points:
            columns[pt[0]].add(pt[1])

        for i,pt1 in enumerate(points):
            for j,pt2 in enumerate(points[i:]):
                if pt1[0]==pt2[0] or pt1[1]==pt2[1]:
                    continue
                
                # if y point of diagonal in column[x of point1] and y of point1 in column[x point of diagonal]
                if pt2[1] in columns[pt1[0]] and pt1[1] in columns[pt2[0]]:
                    
                    curArea = abs(pt2[1]-pt1[1])*abs(pt2[0]-pt1[0])
                    minArea = min(minArea, curArea)
                    
               
        
        return minArea if minArea!=float(\"inf\") else 0 

       
            

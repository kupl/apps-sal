class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        time_points = list()
        
        for interval in A + B:
            time_points.append((interval[0], +1))
            time_points.append((interval[1] + 1, -1))
            
        sorted_points = sorted(time_points, key = lambda x : x[0])
        
        s = 0
        intersect = []
        for i in range(len(sorted_points)):
            s += sorted_points[i][1]
            if i != len(sorted_points)-1 and sorted_points[i][0] == sorted_points[i+1][0]:
                continue
            
            if s == 2:
                intersect.append((sorted_points[i][0], True))
            else:
                intersect.append((sorted_points[i][0], False))
        
        
        i = 0
        ans = list()
        while i < len(intersect):
            while not intersect[i][1]:
                i += 1
                if i == len(intersect):
                    return ans
            ans.append([intersect[i][0], intersect[i+1][0]-1])
            i += 1
            
            
        return ans
                
        


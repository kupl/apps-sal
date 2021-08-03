
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
        
                if pt2[1] in columns[pt1[0]] and pt1[1] in columns[pt2[0]]:
                    
                    curArea = abs(pt2[1]-pt1[1])*abs(pt2[0]-pt1[0])
                    minArea = min(minArea, curArea)
                    
               
        
        return minArea if minArea!=float(\"inf\") else 0 

        # S = set(map(tuple, points))
        # ans = float('inf')
        # for j, p2 in enumerate(points):
        #     for i in range(j):
        #         p1 = points[i]
        #         if (p1[0] != p2[0] and p1[1] != p2[1] and
        #                 (p1[0], p2[1]) in S and (p2[0], p1[1]) in S):
        #             ans = min(ans, abs(p2[0] - p1[0]) * abs(p2[1] - p1[1]))
        # return ans if ans < float('inf') else 0
        
            

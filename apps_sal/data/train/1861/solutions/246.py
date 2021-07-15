class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        rows = defaultdict(set)
        cols = defaultdict(set)
        for i,point in enumerate(points):
            rows[point[0]].add(tuple(point))
            cols[point[1]].add(tuple(point))
            
        minArea = 99999999999
        for point in points:
            rowPoints = rows[point[0]]
            colPoints = cols[point[1]]
            for iP in rowPoints:
                for jP in colPoints:
                    # print(point,iP,jP, (jP[0],iP[1]))
                    if iP[1] > point[1] and jP[0] > point[0] and (jP[0],iP[1]) in rows[jP[0]]:
                        minArea = min(minArea,(iP[1]-point[1])*(jP[0]-point[0]))
                        # print(minArea)
                        
        if minArea == 99999999999:
            return 0
        
        return minArea

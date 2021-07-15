class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        pointrec=dict()
        for x,y in points:
            if not x in pointrec:
                pointrec[x]=dict()
            pointrec[x][y]=1
        area=16*10**8
        for i in range(len(points)-1):
            for j in range(i+1,len(points)):
                a=abs((points[i][0]-points[j][0])*(points[i][1]-points[j][1]))
                if a==0:
                    continue
                if a<area and (points[j][1] in pointrec[points[i][0]]) and (points[i][1] in pointrec[points[j][0]]):
                    area=a
        if area==16*10**8:
            area=0
        return area

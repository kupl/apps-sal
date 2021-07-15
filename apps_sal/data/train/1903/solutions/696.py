class UnionFind:
    def __init__(self):
        self.parent={}
        self.size={}
    def makeset(self,point):
        self.parent[point]=point
        self.size[point]=1
    def find(self,point):
        if self.parent[point]==point:
            return point
        self.parent[point]=self.find(self.parent[point])
        return self.parent[point]
    def union(self,point1,point2):
        point1=self.find(point1)
        point2=self.find(point2)
        if point1==point2:
            return False,self.size[point1]
        self.parent[point2]=point1
        self.size[point1]+=self.size[point2]
        return True,self.size[point1]
        
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        costmetrics=[]
        unionfind=UnionFind()
        for point in points:
            unionfind.makeset(tuple(point))
        # print(unionfind.parent,unionfind.size)
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                cost=abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                costmetrics.append([cost,tuple(points[i]),tuple(points[j])])
        costmetrics.sort(key=lambda item:item[0])
        ans=0
        for i in range(len(costmetrics)):
            res,sz=unionfind.union(costmetrics[i][1],costmetrics[i][2])
            if res:
                ans+=costmetrics[i][0]
            if sz==len(points):
                break
        return ans
            
        
        
                


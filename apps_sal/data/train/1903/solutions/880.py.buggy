class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dis=[[[0,x] for x in range(len(points))] for x in range(len(points))]
        for i,x in enumerate(points):
            for y in range(i+1,len(points)):
                temp=abs(x[0]-points[y][0])+abs(x[1]-points[y][1])
                dis[i][y][0]=temp
                dis[y][i][0]=temp
        for x in range(len(dis)):
            dis[x].sort()
        
        # which I have not included in mst
        rem=[1 for x in range(len(points))]
        
        c=0
        inc={0:1}
        while len(inc)<len(points):
            minn=[float(\"inf\"),-1]
            for x in inc:
                while dis[x][rem[x]][1] in inc:
                    rem[x]+=1
                if dis[x][rem[x]][0]<minn[0]:
                    minn[0],minn[1]=dis[x][rem[x]][0],dis[x][rem[x]][1]
            inc[minn[1]]=1
            c+=minn[0]
        return c
            
        # print(dis)
        

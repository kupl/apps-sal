class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def minnode(vis): 
            mini = 999999999999
            x,y=0,0
        

            # Loop through all the values of 
            # the nodes which are not yet 
            # included in MST and find the 
            # minimum valued one. 
            # k=lambda u,v :u*1+v
            for u,v in points:
                if (vis[(u,v)] == False and dis[(u,v)] < mini): 
                    mini = dis[(u,v)]
                    x,y=u,v
                
            return (mini,x,y)
        
        def cal_cities_dis(x,y):
            dis={}
            vis={}
            for u,v in points:
                vis[(u,v)]=False
                dis[(u,v)]=abs(u-x)+abs(y-v)
            return vis,dis
        
        # Find the rest n-1 nodes of MST. 
        def dist(x,y,u,v):
            
            return abs(u-x)+abs(y-v)
        res=0
        n=len(points)
        
        vis,dis=cal_cities_dis(points[0][0],points[0][1])
        
        # print(vis,dis)
        for i in range(n ): 

            # First find out the minimum node 
            # among the nodes which are not yet 
            # included in MST. 
            c,u,v = minnode( vis) 
            res+=c
            # print(c,u,v)

            # Now the uth node is included in MST. 
            vis[(u,v)]=True

            # Update the values of neighbor 
            # nodes of u which are not yet 
            # included in MST. 
            for x,y in points:
                if ( vis[(x,y)] == False and dist(u,v,x,y)< dis[(x,y)]): 
                    
                    dis[(x,y)] = dist(u,v,x,y)
                
        return res


\t
\t


# This code is contributed by PranchalK 


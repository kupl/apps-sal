class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        def find(e1):
            if a[e1]==-1:
                return e1
            return find(a[e1])
            
        n=len(points)
        a=[-1]*n
        def dist(i,j):
            return abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
        temp=[]
        for i in range(n):
            for j in range(i+1,n):
                temp.append((dist(i,j),i,j))
        temp.sort()
        #print(temp)
        ans=0
        for d,x,y in temp:
            u1,u2=find(x),find(y)
            if u1!=u2:
                a[u2]=u1
                ans+=d
                #print(d,x,y)
        return ans
            
        
        
        


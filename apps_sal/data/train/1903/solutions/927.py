class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        hq = []
        parent = len(points)*[0]
        cnt = len(points)*[0]
        for i in range(len(points)):
            parent[i]=i
            
        for i in range(len(points)-1):
            for j in range(i+1, len(points)):
                dist = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                heappush(hq, [dist, i, j])
        visited = {}
        ans = 0
        
        def find_parent(i):
            if(parent[i]==i):
                return i
            else:
                x = find_parent(parent[i])
                parent[i]=x
                return x
            
        def update_parent(i,j):
            x = find_parent(i)
            y = find_parent(j)
            if(cnt[x]<cnt[y]):
                parent[x]=y
                cnt[y]+=1
            else:
                parent[y]=x
                cnt[x]+=1
            
        while(len(hq)!=0):
            ce = heappop(hq)
            if find_parent(ce[1]) != find_parent(ce[2]):
                ans+=ce[0]
                update_parent(ce[1], ce[2])
        return ans
                


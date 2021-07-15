class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap=[]
        n=len(points)
        for i in range(n-1):
            x1,y1=points[i]
            for j in range(i+1,n):
                x2,y2=points[j]
                heapq.heappush(heap, (abs(x1-x2)+abs(y1-y2), i, j))
        ancient=list(range(n))
        def find(x):
            if x!=ancient[x]:
                ancient[x]=find(ancient[x])
            return ancient[x]
        ans=0
        while heap:
            d,i,j=heapq.heappop(heap)
            ai,aj=find(i), find(j)
            if ai!=aj:
                ancient[ai]=aj
                ans+=d
        return ans

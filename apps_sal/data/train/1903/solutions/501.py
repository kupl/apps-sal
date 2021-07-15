class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def heap_pop(h):
            res=h[0]
            h[0]=h[-1]
            h.pop()
            current=0
            while(2*current+1<len(h)):
                child=2*current+1
                if child+1<len(h):
                    if h[child+1][0]<h[child][0]:
                        child+=1
                if h[current][0]<=h[child][0]:
                    break
                h[current],h[child]=h[child],h[current]
                current=child
            return res
        
        def heap_insert(h,val):
            current=len(h)
            h.append(val)
            while(current>0):
                p=(current-1)//2
                if h[p][0]<=h[current][0]:
                    break
                h[p],h[current]=h[current],h[p]
                current=p
                
        n=len(points)
        dp=[[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                dp[i][j]=abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
        visited=[0 for i in range(n)]
        visited[0]=1
        res=0
        heap=[(dp[0][j],0,j) for j in range(n)]
        heap.sort()
        heap.pop(0)
        while(sum(visited)<n):
            cost,_,current=heap_pop(heap)
            if visited[current]==1:
                continue
            visited[current]=1
            res+=cost
            for j in range(n):
                if visited[j]!=1 and j!=current:
                    heap_insert(heap,(dp[current][j],current,j))
        return res

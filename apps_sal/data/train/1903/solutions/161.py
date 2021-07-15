import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        ans=0
        visit=set()
        x0,y0=points[0]
        N=len(points)
        unvisit=set([i for i in range(1,N)])
        dis=N*[float('inf')]
        cur=0
        while unvisit:
            x0,y0=points[cur]
            for nei in unvisit:
                x1,y1=points[nei]
                dis[nei]=min(dis[nei],abs(x1-x0)+abs(y1-y0))
            cur=min(unvisit,key=lambda x: dis[x])
            ans+=dis[cur]
            unvisit.remove(cur)
        return ans
        
        
        
        
        \"\"\"
        xlist=[]
        ylist=[]
        for x,y in points:
            xlist.append(x)
            ylist.append(y)
        def partition(A,l,r):
            left,right=l,l
            pivot=A[r-1]
            for right in range(l,r):
                if A[right]<=pivot:
                    A[right],A[left]=A[left],A[right]
                    left+=1
            return left
        def medium(A):
            random.shuffle(A)
            N=len(A)
            left,right=0,N
            M=(N+1)//2
            z=-1
            while z!=M:
                z=partition(A,left,right)
                if z==M:
                    return A[z-1]
                elif z>M:
                    right=z-1
                else:
                    left=z
                partition(A,left,right)
        xm=medium(xlist)
        ym=medium(ylist)
        ans=0
        for x,y in points:
            ans+=abs(x-xm)
            ans+=abs(y-ym)
        return ans
        \"\"\"       
            
                

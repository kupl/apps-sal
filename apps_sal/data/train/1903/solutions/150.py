class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def get_dist(p,q):
            return abs(p[0]-q[0])+abs(p[1]-q[1])
        
        n=len(points)
        seen=set()
        dist=[math.inf]*n
        res=0
        cur=0
        for i in range(n-1):
            seen.add(cur)
            for j in range(n):
                if j in seen:
                    continue
                d=get_dist(points[cur],points[j])
                dist[j]=min(dist[j],d)
            
            delta,cur=min((d,j) for j,d in enumerate(dist))
            res+=delta
            dist[cur]=math.inf
        return res

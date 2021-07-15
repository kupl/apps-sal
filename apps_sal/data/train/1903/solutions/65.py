class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if len(points) == 1: return 0
        res = 0
        curr = 0 # select a random point as the starting point
        dis = [math.inf] * n
        explored = set()
        
        for i in range(n - 1):
            x0, y0 = points[curr]
            explored.add(curr)
            for j, (x, y) in enumerate(points):
                if j in explored: continue
                dis[j] = min(dis[j], abs(x - x0) + abs(y - y0))
                
            delta, curr = min((d, j) for j, d in enumerate(dis)) 
            dis[curr] = math.inf
            res += delta
            
        return res    
    def minCostConnectPoints2(self, P: List[List[int]]) -> int:
        res=0
        n=len(P)
        px,py=P[0]
        seen={0}
        todo=set(range(1,n))
        while len(seen)<n:
            mn=float('inf')
            used=-1
            for i in todo:
                cx,cy=P[i]
                for j in seen:
                    px,py=P[j]
                    can=abs(cx-px)+abs(cy-py)
                    if can <mn:
                        mn=can
                        used=i
            res+=mn
            todo.remove(used)
            seen.add(used)
        return res

    # def minCostConnectPoints1(self, P: List[List[int]]) -> int:
    #     P.sort(key=lambda a:(abs(a[0])+abs(a[1])))
    #     print(P)
    #     res=0
    #     px,py=P[0]
    #     for cx,cy in P[1:]:
    #         res+=abs(cx-px)+abs(cy-py)
    #         px,py=cx,cy
    #     return res    


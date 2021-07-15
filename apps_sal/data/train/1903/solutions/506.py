class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points)<=1:
            return 0
        prior=[[] for _ in points]
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                dist=abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                prior[i].append((dist,j))
                prior[j].append((dist,i))
        heapify(prior[0])
        seen=set([0])
        cur=prior[0]
        res=0
        while len(seen)<len(points):
            dist,tar=heappop(cur)
            if tar not in seen:
                res+=dist
                seen.add(tar)
                for d,t in prior[tar]:
                    if t not in seen:
                        heappush(cur,(d,t))
        return res

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def dist(a,b,c,d):
            return abs(a-c)+abs(b-d)
        res = 0
        if len(points) <= 1: return 0
        r = 0
        visited = set()
        k = defaultdict(lambda:999999999)
        k[tuple(points[0])] = 0 # source vertex
        for _ in range(len(points)):
            m = float('inf')
            cand = ()
            for point in k:
                if k[point] < m and point not in visited:
                    cand = point
                    m = k[point]
            visited.add(cand)
            
            for point in points:
                p = tuple(point)
                if p != cand and p not in visited and dist(cand[0], cand[1], p[0], p[1]) < k[p]:
                    k[p] = dist(cand[0], cand[1], p[0], p[1]) 
                    # res += k[p]
        print((k, sum(k.values())))
    
        return sum(k.values())


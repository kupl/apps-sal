class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dis = []
        d = {}
        u = {}
        for i,x in enumerate(points):
            d[i] = 0
            u[i] = i
            for y in range(i+1,len(points)):
                z = points[y]
                m = abs(x[0]-z[0]) + abs(x[1]-z[1])
                dis.append([m,i,y])
        
        def merge(c1,c2):
            if u[c1] > u[c2]:
                c1,c2 = c2,c1
            t = u[c2]
            for k,v in u.items():
                if v == t:
                    u[k] = u[c1]
        
        dis = sorted(dis)
        c = 0
        result = 0
        count=0
        while count < len(points) - 1:
            while 1:
                c0,c1,c2 = dis[c]
                if u[c1] != u[c2]:
                    merge(c1,c2)
                    d[c1] += 1
                    d[c2] += 1
                    count += 1
                    result += c0
                    c += 1
                    break
                c += 1
        return result

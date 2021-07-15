class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        s = [0]
        res = 0
        d = {i: abs(points[i][0]-points[0][0]) + abs(points[i][1]-points[0][1]) for i in range(len(points))}
        current = 0
        while len(s) < len(points):
            min_ = float('inf')
            next_ = current
            for i in range(1,len(points)):
                if d[i] == 0:
                    continue
                else:
                    dis = abs(points[i][0]-points[next_][0]) + abs(points[i][1]-points[next_][1])
                    if dis <= d[i]:
                        d[i] = dis
                    if d[i] <= min_:
                        min_ = d[i]
                        current = i
            res += min_
            d[current] = 0
            s.append(current)
        return res
                                                                    
            
        
                    


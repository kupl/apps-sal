class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0
        
        neibors = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                point1 = points[i]
                point2 = points[j]
                dis = abs(point1[0]-point2[0]) + abs(point1[1]-point2[1])
                neibors.append((dis, i, j))
        neibors_sorted = sorted(neibors)
        
        unions = {i:i for i in range(len(points))}
        
        def find(i):
            if unions[i] == i:
                return i
            else:
                unions[i] = find(unions[i])
                return unions[i]
        
        ret = 0
        line = 0
        for neibor in neibors_sorted:
            if find(neibor[1]) != find(neibor[2]):
                unions[find(neibor[1])] = find(neibor[2])
                ret += neibor[0]
                line += 1
                if line == (len(points)-1):
                    return ret
            else:
                continue
            
            
            
        
        
        
        
        
        
        
        
        
        


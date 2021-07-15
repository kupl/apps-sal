class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        x_set = set()
        points = []
        
        for x1, y1, x2, y2 in rectangles:
            x_set.add(x1)
            x_set.add(x2)
            heapq.heappush(points, (y1, x1, x2, 1))
            heapq.heappush(points, (y2, x1, x2, -1))
        
        x_list = sorted(list(x_set))
        mapping = {x: i for i, x in enumerate(x_list)}
        count = [0]*len(x_list)
        
        res = 0
        pre_y = points[0][0]
        
        while points:
            cur_y = points[0][0]
            h = cur_y-pre_y
            for i in range(len(x_list)-1):
                if count[i] > 0:
                    res += (x_list[i+1]-x_list[i])*h
            res %= (10**9+7)
            
            while points and points[0][0] == cur_y:
                cur_y, x1, x2, cnt = heapq.heappop(points)
                for i in range(mapping[x1], mapping[x2]):
                    count[i] += cnt
            
            pre_y = cur_y
        
        return res

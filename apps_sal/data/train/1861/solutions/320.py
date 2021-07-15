class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        
        # 针对每一组点, check 有没有另外两个点可以组成一个长方形
        # (1, 2) 和 (4, 3), 检查有没有 (1, 3) 和 (4, 2)
        
        points_set = set(map(tuple, points))
        min_area = float('inf')
        
        for idx, p2 in enumerate(points):
            for i in range(idx):
                p1 = points[i]
                if p1[0] != p2[0] and p1[1] != p2[1] and (p1[0], p2[1]) in points_set and (p2[0], p1[1]) in points_set:
                    area = abs( (p2[0]-p1[0])*(p2[1] - p1[1]) )
                    min_area = min(min_area, area)
        
        return min_area if min_area < float('inf') else 0
        
        


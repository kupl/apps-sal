class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        
        x_to_ys = collections.defaultdict(set)
        for px, py in points:
            x_to_ys[px].add(py)
            
        min_area = float(\"inf\")
        xs = sorted(list(x_to_ys.keys()))
        for i, x1 in enumerate(xs):
            for j in range(i+1, len(xs)):
                x2 = xs[j]
                if x2-x1>min_area:
                    break
                common_ys = x_to_ys[x1] & x_to_ys[x2]
                if len(common_ys)>=2:
                    common_ys = sorted(list(common_ys))
                    min_y_diff = min(y-common_ys[iy] 
                                     for iy, y in enumerate(common_ys[1:]))
                    min_area = min(min_area, min_y_diff*(x2-x1))
                
        if min_area==float(\"inf\"):
            return 0
        else:
            return min_area

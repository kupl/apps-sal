from collections import defaultdict

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        xs = defaultdict(list)
        ys = defaultdict(list)
        hm = defaultdict(bool)

        for point in points:
            xs[point[0]] += [point]
            ys[point[1]] += [point]
            hm[tuple(point)] = True 

        min_area = float(\"inf\")
        for p1 in points:
            # get all points on the same y as p1 that are 
            same_y = [(x,y) for x,y in ys[p1[1]] if x > p1[0]]
            same_x = [(x,y) for x,y in xs[p1[0]] if y > p1[1]]

            for p2 in same_y:
                for p3 in same_x:
                    p4 = (p2[0], p3[1])
                    if hm[p4]:
                        dx = abs(p2[0]-p1[0])
                        dy = abs(p3[1]-p1[1])
                        min_area = min(min_area, dx*dy)

        return min_area if min_area < float(\"inf\") else 0

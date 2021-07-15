from functools import reduce
class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        def intersection(a, b):
            return [max(a[0], b[0]), max(a[1], b[1]), min(a[2], b[2]), min(a[3], b[3])]
        
        def area(rec):
            dx = max(0, rec[2] - rec[0])  # <================== need to use max!!!
            dy = max(0, rec[3] - rec[1])
            return dx * dy
        
        import itertools
        a = 0
        for i in range(1, len(rectangles) + 1):
            sign = (-1) ** (i + 1)
            for k in itertools.combinations(rectangles, i):
                a += sign * area(reduce(intersection, k))

        return a % (10**9 + 7)
    
    #50
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        
        xmap = [{}, {}]
        xs = [[], []]

        for i in rectangles:
            xs[0].append(i[0])
            xs[0].append(i[2])
            xs[1].append(i[1])
            xs[1].append(i[3])
        xs[0].sort()
        xs[1].sort()
        # print(xs)
        rmap = [[], []]
        for k in range(2):
            cnt = 0
            for i in xs[k]:
                if i not in xmap[k]:
                    xmap[k][i] = cnt
                    rmap[k].append(i)
                    cnt += 1
        # print(rmap)
        grid = [[0] * len(rmap[0]) for _ in range(len(rmap[1]))]  # donnot add extra []

        for r in rectangles:
            for i in range(xmap[0][r[0]], xmap[0][r[2]]):
                for j in range(xmap[1][r[1]], xmap[1][r[3]]):
                    # print(i, j, len(grid), len(grid[0]))
                    grid[j][i] = 1   # <========================= not [i][j]
        
        area = 0
        for i in range(len(rmap[0]) - 1):
            width = rmap[0][i + 1] - rmap[0][i]
            for j in range(len(rmap[1]) - 1):
                if grid[j][i]:
                    area += width * (rmap[1][j + 1] - rmap[1][j])
        return area % (10**9 + 7)
            
        
                
        



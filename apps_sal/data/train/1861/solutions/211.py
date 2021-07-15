class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: (x[0], x[1]))
        self.res = float('inf')
        self.cache = defaultdict(list)
        
        x_cache = defaultdict(list)
        
        for x,y in points:
            for y2 in x_cache[x]:
                if y2 < y:
                    for x_other in self.cache[(y, y2)]:
                        self.res = min(self.res, abs(x_other-x) * abs(y2-y))
                    self.cache[(y, y2)].append(x)
            x_cache[x].append(y)
        if self.res == float('inf'):
            self.res = 0
        return self.res

import random

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> int:
        l, h, k = 0, len(points) - 1, K - 1
        
        dist = lambda i : points[i][0] ** 2 + points[i][1] ** 2
        
        def partition(l: int, h: int) -> int:
            t = random.randint(l, h)
            points[t], points[h] = points[h], points[t]
            for i, val in enumerate(points[l:h+1], l):
                if dist(i) < dist(h):
                    points[i], points[l] = points[l], points[i]
                    l += 1
            points[l], points[h] = points[h], points[l]
            return l
        
        
        while True:
            pos = partition(l, h)
            if pos < k:
                l = pos + 1
            elif pos > k:
                h = pos - 1
            else:
                return points[:K]
                    


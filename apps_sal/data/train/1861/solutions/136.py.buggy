class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        lookup = set()
        for x, y in points:
            lookup.add((x, y))
        
        res = float(\"inf\")
        for x1, y1 in points:              ##在points里面遍历！！定下两个点就可以确定一个矩形,
            for x2, y2 in points:
                if x1 > x2 and y1 > y2:  ##去掉之前看过的元素！！
                    if (x1, y2) in lookup and (x2, y1) in lookup:
                  
                        res = min(res, abs(x1 - x2) * abs(y1 - y2))
        
        if res < float(\"inf\"):
            return res
        else:
            return 0
            

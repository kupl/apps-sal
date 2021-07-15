class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        # the key point of this solution is how do we generate a list of rectangles that don't overlap with each other. The idea is that we try to add each new rectangle into the list. If it has overlap with existing rectangles, then we break it into muliple parts that don't have overlap with existing rectangles.
        all_rectangles = []
        for rectangle in rectangles:
            self.add_rectangle(all_rectangles, rectangle, 0)
        
        ans = 0
        mod = pow(10, 9) + 7
        for rect in all_rectangles:
            x1, y1, x2, y2 = rect
            ans += ((x2 - x1) * (y2 - y1)) % mod
        
        return ans % mod
    
    def add_rectangle(self, all_rectangles, cur, start):
        if start >= len(all_rectangles):
            all_rectangles.append(cur)
            return
        
        x1, y1, x2, y2 = cur
        rx1, ry1, rx2, ry2 = all_rectangles[start]
        
        if x2 <= rx1 or x1 >= rx2 or y2 <= ry1 or y1 >= ry2:
            self.add_rectangle(all_rectangles, cur, start + 1)
            return
        
        if x1 < rx1:
            self.add_rectangle(all_rectangles, [x1, y1, rx1, y2], start + 1)
        
        if x2 > rx2:
            self.add_rectangle(all_rectangles, [rx2, y1, x2, y2], start + 1)
        
        if y1 < ry1:
            self.add_rectangle(all_rectangles, [max(x1, rx1), y1, min(x2, rx2), ry1], start + 1)
        
        if y2 > ry2:
            self.add_rectangle(all_rectangles, [max(x1, rx1), ry2, min(x2, rx2), y2], start + 1)


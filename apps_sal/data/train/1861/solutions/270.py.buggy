\"\"\"
solution 2: O(N^2)
我们choose two diagnol points to iterate - then check if other two diagonal points in p_set
\"\"\"
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        p_set = set(map(tuple, points))     # 变成set, 这样查找更快

        # 注意我们choose two diagnol points to iterate
        min_area = float(\"inf\")
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1 == x2 or y1 == y2:    # diagonal元素必须不能平行于x-axes or y-axes
                    continue
                x3, y3 = x2, y1
                x4, y4 = x1, y2
                if (x3, y3) in p_set and (x4, y4) in p_set:
                    min_area = min(min_area, abs(x1 - x2) * abs(y1 - y2))

        return 0 if min_area == float(\"inf\") else min_area

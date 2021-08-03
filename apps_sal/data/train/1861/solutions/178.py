class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        from collections import defaultdict

        x_dic = defaultdict(list)
        y_dic = defaultdict(list)

        area = float('inf')

        for x, y in points:
            x_dic[x].append(y)
            y_dic[y].append(x)

            for _y in x_dic[x]:
                if _y != y and _y in y_dic:
                    for _x in y_dic[_y]:
                        if _x != x and _x in x_dic and y in x_dic[_x]:
                            area = min(area, abs(x - _x) * abs(y - _y))

        return area if area < float('inf') else 0

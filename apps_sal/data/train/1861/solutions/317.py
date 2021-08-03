from collections import defaultdict


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        res = float('inf')
        past_points = set()
        for x1, y1 in points:
            for x2, y2 in past_points:
                if x1 != x2 and y1 != y2:
                    if (x1, y2) in past_points and (x2, y1) in past_points:
                        area = abs(x1 - x2) * abs(y1 - y2)
                        res = min(res, area)
            past_points.add((x1, y1))
        # for cur_point in points:
        #     for dia_point in points:
        #         if cur_point[0] != dia_point[0] and cur_point[1] != dia_point[1]:
        #             if (cur_point[0], dia_point[1]) in past_points \\
        #             and (dia_point[0], cur_point[1]) in past_points:
        #                 new_area = abs(cur_point[0]-dia_point[0]) * abs(cur_point[1]-dia_point[1])
        #                 print(new_area)
        #                 res = min(res, new_area)
        #     past_points.add((cur_point[0], cur_point[1]))
        return res if res != float('inf') else 0

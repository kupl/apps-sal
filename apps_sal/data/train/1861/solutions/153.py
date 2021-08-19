class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        if len(points) < 4:
            return 0
        # watch for degenerate cases of 4 same points or getting a line
        # if points weren't distinct, can convert to set and then back to list
        # for every x, need list of y's (set)
        # for every y, need list of x's (set)
        # then, O(4) to find a rectangle
        # x_vals: {1: [1, 3], 3: [3, 1], 2: [2]}
        # y_vals: {1, [1, 3], 3: [3, 1], 2: [2]}

        # Then, to check, loop through all x's and see if we can get all 4 points for each; if so, calculate area

        # Runtime: O(n^3)
        # x_vals = defaultdict(set)
        # y_vals = defaultdict(set)
        # for p in points:
        #     x_vals[p[0]].add(p[1])
        #     y_vals[p[1]].add(p[0])
        # # print(x_vals)
        # # print(y_vals)
        # min_area = 40000*40000 + 1
        # for x, y_coords in x_vals.items():
        #     if len(y_coords) == 1:
        #         continue # can't make a rectangle if it's the only point on that x = x line
        #     y_list = list(y_coords)
        #     for i, y_1 in enumerate(y_list):
        #         for j, y_2 in enumerate(y_list[i+1:]):
        #             # we have points (x, y_1) and (x, y_2)
        #             # now need to check if same value in both y_vals[y_1] and y_vals[y_2]
        #             # if so, we have a rectangle!
        #             common_x_2 = y_vals[y_1].intersection(y_vals[y_2])
        #             common_x_2.remove(x) # avoid degenerate case of a line
        #             for x_2 in list(common_x_2):
        #                 # print(x, x_2, y_1, y_2)
        #                 min_area = min(min_area, abs(x_2 - x) * abs(y_2 - y_1))
        # if min_area == 40000*40000 + 1:
        #     return 0
        # return min_area

        # Improved O(n^2) solution that's a lot simpler too:
        min_area = 40000 * 40000 + 1
        seen_points = set()
        for x, y in points:
            seen_points.add((x, y))
        # print(seen_points)
        for p1_x, p1_y in points:
            for p2_x, p2_y in points:
                if p1_x > p2_x and p1_y > p2_y:
                    if (p1_x, p2_y) in seen_points and (p2_x, p1_y) in seen_points:
                        area = abs(p2_x - p1_x) * abs(p2_y - p1_y)
                        if area > 0:
                            min_area = min(min_area, area)
        if min_area == 40000 * 40000 + 1:
            return 0
        return min_area

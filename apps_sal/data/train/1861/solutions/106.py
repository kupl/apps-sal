class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        if len(points) < 4:
            return 0
        group_x_coords = collections.defaultdict(list)
        group_y_coords = collections.defaultdict(set)
        for point in points:
            group_x_coords[point[0]].append(point[1])
            group_y_coords[point[1]].add(point[0])
        min_area = float('inf')
        for key in group_x_coords.keys():
            if len(group_x_coords[key]) < 2:
                continue
            for i in range(len(group_x_coords[key])):
                for j in range(i + 1, len(group_x_coords[key])):
                    y_val_1 = group_x_coords[key][i]
                    y_val_2 = group_x_coords[key][j]
                    common_x_coords = group_y_coords[y_val_1] & group_y_coords[y_val_2]
                    if len(common_x_coords) > 1:
                        y_diff = abs(y_val_1 - y_val_2)
                        x_diff = float('inf')
                        for ele in common_x_coords:
                            if ele == key:
                                continue
                            if abs(ele - key) < x_diff:
                                x_diff = abs(ele - key)
                        area = x_diff * y_diff
                        if area < min_area:
                            min_area = area
        if min_area == float('inf'):
            return 0
        return min_area

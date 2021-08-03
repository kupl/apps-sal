class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        area = float('inf')
        x_order = collections.defaultdict(list)
        y_order = collections.defaultdict(list)
        for p in points:
            x_order[p[0]].append(p[1])
            y_order[p[1]].append(p[0])

        xs = sorted(list(x_order.items()), key=lambda x: x[0])
        for col in xs:
            if len(col[1]) < 2:
                continue

            for i in range(len(col[1]) - 1):
                j = i + 1
                while j < len(col[1]):
                    common_x = list(set(y_order[col[1][i]]) & set(y_order[col[1][j]]))
                    # remove the side of the col we hold now
                    common_x.remove(col[0])
                    if common_x:
                        for x in common_x:
                            a = (abs(col[0] - x) * abs(col[1][i] - col[1][j]))
                            area = min(area, a)
                    j += 1
        return area if area < float('inf') else 0

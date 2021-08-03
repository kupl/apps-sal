from collections import defaultdict


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        x_groups = defaultdict(list)
        for pnt in points:
            x_groups[pnt[0]].append(pnt[1])

        pair2x = dict()

        min_area = float('inf')
        for x in sorted(x_groups):
            group = x_groups[x]
            group.sort()

            for i in range(len(group)):
                for j in range(i + 1, len(group)):
                    last_x = pair2x.get((group[i], group[j]))
                    if last_x is not None:
                        min_area = min(min_area, (x - last_x) * (group[j] - group[i]))
                    pair2x[group[i], group[j]] = x

        return min_area if min_area < float('inf') else 0

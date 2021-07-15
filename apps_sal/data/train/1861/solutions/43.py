import collections as clc
import itertools as it


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        xs = set()
        ys = set()
        for x, y in points:
            xs.add(x)
            ys.add(y)
        ys_at = clc.defaultdict(list)
        if len(xs) > len(ys):
            for x, y in points:
                ys_at[x].append(y)
        else:
            for x, y in points:
                ys_at[y].append(x)
        latest_x = {}
        ans = float(\"inf\")
        for x in sorted(ys_at):
            for y1, y2 in it.combinations(ys_at[x], 2):
                y1, y2 = sorted([y1, y2])
                if (y1, y2) in latest_x:
                    ans = min(ans, (x - latest_x[y1, y2]) * (y2 - y1))
                latest_x[y1, y2] = x
        return ans if ans != float(\"inf\") else 0

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        import math
        from collections import defaultdict
        row_m = defaultdict(set)
        rows = set()
        for x, y in points:
            row_m[x].add(y)
            rows.add(x)

        rows = sorted(rows)
        l = len(rows)
        sol = math.inf
        print(rows)
        for i in range(l):
            x1 = rows[i]
            for j in range(i + 1, l):
                x2 = rows[j]

                # print(\"x1\", x1, \"x2\", x2)
                row1 = row_m[x1]
                row2 = row_m[x2]

                intersect = sorted(set(row1) & set(row2))

                if len(intersect) < 1:
                    continue

                smallest = math.inf
                for i, point in enumerate(intersect[1:], start=1):
                    # print(\"point\", point, i, intersect[i - 1])
                    smallest = min(
                        smallest,
                        point - intersect[i - 1]
                    )
                # print(\"smallest\", smallest, intersect)
                sol = min(
                    sol,
                    smallest * (x2 - x1),
                )

        if sol is math.inf:
            return 0
        return sol

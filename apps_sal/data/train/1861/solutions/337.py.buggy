from collections import defaultdict

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        # Sort by Column
        # Time  complexity: O(N^2)
        # Space complexity: O(N)
        # columns = defaultdict(list)
        # for x, y in points:
        #     columns[x].append(y)
        # lastx, ans = {}, float(\"inf\")

        # for x in sorted(columns):
        #     column = columns[x]
        #     column.sort()
        #     for j, y2 in enumerate(column):
        #         for i in range(j):
        #             y1 = column[i]
        #             if (y1, y2) in lastx:
        #                 ans = min(ans, (x - lastx[y1, y2]) * (y2 - y1))
        #             lastx[y1, y2] = x

        # return ans if ans < float(\"inf\") else 0


        # Count by Diagonal
        # For each pair of points in the array, consider them to be the long diagonal of a potential rectangle. We can check if all 4 points are there using a Set.
        # Time  complexity: O(N^2)
        # Space complexity: O(N)
        S = set(map(tuple, points))
        ans = float(\"inf\")
        for j, p2 in enumerate(points):
            for i in range(j):
                p1 = points[i]
                if p1[0] != p2[0] and p1[1] != p2[1] and \\
                    (p1[0], p2[1]) in S and (p2[0], p1[1]) in S:
                    ans = min(ans, abs(p2[0] - p1[0]) * abs(p2[1] - p1[1]))
        return ans if ans < float(\"inf\") else 0
        

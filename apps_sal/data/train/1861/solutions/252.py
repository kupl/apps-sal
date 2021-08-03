class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        '''
        Count by diagonal - approach 2 in solution

        https://leetcode.com/problems/minimum-area-rectangle/discuss/240341/Python-O(n2)-easy-to-understand.-Good-for-beginners
        '''

        if not points:
            return 0

        points_table = set()
        for x, y in points:
            points_table.add((x, y))

        min_area = float('inf')
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                '''
                check for diagonal only
                '''
                if x1 != x2 and y1 != y2:
                    if (x1, y2) in points_table and (x2, y1) in points_table:
                        min_area = min(min_area, abs(x1 - x2) * abs(y1 - y2))

        return 0 if min_area == float('inf') else min_area

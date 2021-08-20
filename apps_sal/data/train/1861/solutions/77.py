class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        seen = set()
        minv = float('inf')
        for (x, y) in points:
            for (a, b) in seen:
                if x != a and y != b and ((x, b) in seen) and ((a, y) in seen):
                    minv = min(minv, abs(a - x) * abs(y - b))
            seen.add((x, y))
        return minv if minv != float('inf') else 0

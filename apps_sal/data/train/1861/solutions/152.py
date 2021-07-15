class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        saw = set()
        res = float('inf')
        for x, y in points:
            for dx, dy in saw:
                p1 = (dx, y)
                p2 = (x, dy)
                if p1 in saw and p2 in saw and dx != x and dy != y:
                    res = min(res, abs(dx - x) * abs(dy - y))
            saw.add((x, y))
        return res if res != float('inf') else 0

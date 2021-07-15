class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def helper(p):
            return p[0]**2 + p[1]**2
        return sorted(points, key=helper)[:K]

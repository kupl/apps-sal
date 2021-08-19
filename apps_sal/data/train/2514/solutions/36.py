class Solution:

    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        dist_matrix = [all((abs(x - y) > d for y in arr2)) for x in arr1]
        return sum(dist_matrix)

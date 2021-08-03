class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:

        dist_matrix = [[abs(x - y) for y in arr2] for x in arr1]

        return len([1 for dist_lst in dist_matrix if min(dist_lst) > d])

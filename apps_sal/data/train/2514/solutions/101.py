class Solution:

    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        return len([g for g in [min(k) for k in [[abs(t - y) for t in arr2] for y in arr1]] if g > d])

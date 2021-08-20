class Solution:

    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        forbid_set = set()
        for a2 in arr2:
            forbid_set |= set(range(a2 - d, a2 + d + 1))
        return sum((1 for a1 in arr1 if a1 not in forbid_set))

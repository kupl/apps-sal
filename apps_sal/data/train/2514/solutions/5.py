class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        return sum([sum([abs(a - b) > d for b in arr2]) == len(arr2) for a in arr1])

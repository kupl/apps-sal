class Solution:

    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
        for a in set(arr1):
            if all((abs(a - b) > d for b in set(arr2))):
                count += arr1.count(a)
        return count

class Solution:

    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        total = 0
        for n in arr1:
            if all((abs(n - _n) > d for _n in arr2)):
                total += 1
        return total

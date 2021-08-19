class Solution:

    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
        for i in arr1:
            curr = 0
            for j in arr2:
                if abs(i - j) <= d:
                    curr += 1
            if curr == 0:
                count += 1
        return count

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        ans = 0
        for i in arr1:
            is_valid = True
            for j in arr2:
                if abs(i-j)<=d:
                    is_valid = False
                    break
            if is_valid:
                ans += 1
        return ans

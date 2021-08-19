class Solution:

    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        ans = 0
        for i in arr1:
            for j in range(i - d, i + d + 1):
                if j in arr2:
                    break
            else:
                ans += 1
        return ans

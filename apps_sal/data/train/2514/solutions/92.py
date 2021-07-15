class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        ans = 0
        for x in arr1:
            ans += all([abs(x-y) > d for y in arr2])
        return ans


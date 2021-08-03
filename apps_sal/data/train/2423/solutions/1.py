class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minVal = 1
        t = 0
        for num in nums:
            t += num
            if(t < 0):
                minVal = max(1 - t, minVal)
        return minVal

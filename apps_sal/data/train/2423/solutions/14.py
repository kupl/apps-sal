class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        res = 0
        cur = 0
        for num in nums:
            cur += num
            if cur < 1:
                res += 1 - cur
                cur += 1 - cur
        if res == 0:
            return 1
        return res

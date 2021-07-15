class Solution:
    def specialArray(self, nums: List[int]) -> int:
        x = 0
        res = 0
        maxn = max(nums)
        # minn = min(nums)
        for i in range(maxn+1):
            res = 0
            for y in nums:
                if y >= i:
                    res += 1
            if res == i:
                return i
        return -1


class Solution:

    def specialArray(self, nums: List[int]) -> int:
        x = None
        for i in range(1, len(nums) + 1):
            count = 0
            for n in nums:
                if n >= i:
                    count += 1
            if count == i:
                x = i
                break
        return x if x is not None else -1

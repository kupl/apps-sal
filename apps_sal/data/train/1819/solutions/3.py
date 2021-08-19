class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        import random
        # if only one element
        if len(self.nums) == 1:
            return 0

        ans = -1
        idx = 0
        for i, num in enumerate(self.nums):
            if num == target:
                if ans == -1:
                    ans = i
                else:
                    if random.randint(0, idx) == 0:
                        ans = i
                idx += 1
        return ans

        # result = -1
        # index = 0
        # for i in range(0, len(self.nums), 1):
        #     if self.nums[i] == target:
        #         if result == -1:
        #             result = i
        #         else:
        #             if random.randint(0, index) == 0:
        #                 result = i
        #         index += 1
        # return result


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

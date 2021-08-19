class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:

        # while nums:
        #     for i in range(1,len(nums)+1):
        #         if i == len(nums): return step
        #         if nums[i] <= nums[i-1]:
        #             step += nums[i-1] - nums[i] + 1
        #             nums[i] += nums[i-1] - nums[i] + 1
        #             nums = nums[i:]
        #             break
        # return step
        step = 0
        if not A or len(A) == 1:
            return step
        prev = float('-inf')
        nums = sorted(A)
        for e in nums:
            if e <= prev:
                step += prev - e + 1
                prev += 1
            else:
                prev = e
        return step

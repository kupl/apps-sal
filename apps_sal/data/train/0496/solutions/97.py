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
        step = curr = 0

        for e in sorted(A):

            step += max(curr - e, 0)
            curr = max(curr, e) + 1
        return step

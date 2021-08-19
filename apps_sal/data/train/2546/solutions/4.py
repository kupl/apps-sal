class Solution:

    def numIdenticalPairs(self, nums: List[int]) -> int:
        num_good = 0
        for i in range(len(nums)):
            first = nums[i]
            for j in nums[i + 1:]:
                print((first, j))
                if first == j:
                    num_good += 1
        return num_good

class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        my_list = []
        for (index, num) in enumerate(nums):
            for n in nums[index + 1:]:
                my_list.append((num - 1) * (n - 1))
        return max(my_list)

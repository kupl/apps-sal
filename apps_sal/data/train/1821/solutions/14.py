class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        start_node = (length - 2) // 2
        for i in range(start_node, -1, -1):
            self.build(nums, i, length)
        for i in range(length - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.build(nums, 0, i)
        return nums
#     def sortArray(self, nums: List[int]) -> List[int]:
#         length = len(nums)
#         for i in range(length - 1, -1, -1):
#             self.build(nums, i, length)

#         for i in range(length - 1, 0, -1):
#             nums[0], nums[i] = nums[i], nums[0]
#             self.build(nums, 0, i)
#         return nums

    def build(self, nums, node, n):
        left = node * 2 + 1
        right = node * 2 + 2
        large = node

        if left < n and nums[left] > nums[large]:
            large = left
        if right < n and nums[right] > nums[large]:
            large = right
        if large != node:
            nums[large], nums[node] = nums[node], nums[large]
            self.build(nums, large, n)

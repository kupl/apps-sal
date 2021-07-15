class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        for i in range(length - 1, -1, -1):
            self.maxheap(nums, length, i)
        
        for i in range(length - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.maxheap(nums, i, 0)
        return nums


    def maxheap(self, nums, n, node):
        l = node * 2 + 1
        r = node * 2 + 2
        large = node

        if l < n and nums[l] > nums[large]:
            large = l
        if r < n and nums[r] > nums[large]:
            large = r
        if large != node:
            nums[node], nums[large] = nums[large], nums[node]
            self.maxheap(nums, n, large)


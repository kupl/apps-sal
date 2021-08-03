class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.quickSort(nums)

    def quickSort(self, nums):
        if not nums or len(nums) < 2:
            return nums
        pivot = nums[0]
        left = []
        right = []
        for x in nums[1:]:
            if x <= pivot:
                left.append(x)
            else:
                right.append(x)
        return self.quickSort(left) + [pivot] + self.quickSort(right)

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.qsort(nums, 0, len(nums))
        return nums
    
    def qsort(self, nums, begin, end):
        if begin>=end:
            return
        x = nums[end-1]
        i = j = begin
        while j<end-1:
            if nums[j]<x:
                self.swap(nums, i, j)
                i += 1
            j += 1
        self.swap(nums, i, j)
        self.qsort(nums, begin, i)
        self.qsort(nums, i+1, end)
        
    def swap(self, nums, i, j):
        a = nums[i]
        nums[i] = nums[j]
        nums[j] = a

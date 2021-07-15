class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.quickSort(nums)
    
    def quickSort(self, nums):
        if not nums or len(nums) < 2:
            return nums
        
        pivot = nums[0]
        left = []
        right = []
        for n in nums[1:]:
            if n <= pivot:
                left.append(n)
            else:
                right.append(n)
        return self.quickSort(left) + [pivot] + self.quickSort(right)
                
        
        


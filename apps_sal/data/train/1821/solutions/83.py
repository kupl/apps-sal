class Solution:
    def sortArray(self, nums: List[int]):
        #use qsort, lc 215
        #partition() will place the pivot into the correct place, 左閉右閉
        #outer function, will recursively process the numbers nums[:correct_idx] and numbers nums[correct_idx+1:] 
        #qsort(nums[4,3,6,6,8,6], 4 will be placed to idx1 => [3,4,6,6,8,6])
        # /                 \\
        #qsort(nums[3])    qsort([6,6,8,6], 6 will be placed to idx 2 in the original nums)
        
        #=>qsort() is the recursion, with input arg as start idx, end idx
        
        self.qsort(nums, 0, len(nums)-1)
        return nums
    
    def qsort(self, nums, start_idx, end_idx): #start_idx and end_idx 左閉右閉
        
        #terminate:
        #if end_idx >= start_idx: => error
        if end_idx <= start_idx:
            return
        
        #start_idx = 0
        #end_idx = len(nums)-1
        correct_idx = self.partition(nums, start_idx, end_idx) #the partition() will put nums[start] into the correct place
        self.qsort(nums, start_idx, correct_idx-1)
        self.qsort(nums, correct_idx+1, end_idx)
        
    def partition(self, nums, start, end):
        pivot = nums[start]
        left = start + 1
        right = end
        
        #goal: put values <= pivot before pointer left
        #                 >=       after pointer right
        while left <= right:
            #if nums[left] > pivot: #now we need to find the nums[right] < pivot so that we can swap them
            
            if nums[left] > pivot and nums[right] < pivot:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            if nums[left] <= pivot:
                left += 1
            if nums[right] >= pivot:
                right -= 1
        
        #now right is the correct place  to place pivot
        nums[start], nums[right] = nums[right], nums[start]
        return right


\"\"\"

                e
            5 2 1 3 
                  s 

pivot = nums[s] = 5

We need to have nums[s] < pviot < nums[e]

if nums[s] > pivot and nums[e] < pivot: out of place so swap(nums, s, e)

if nums[s] <= pivot : right place s += 1

if nums[l] >= pivot : right place l -= 1

\"\"\"


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        self.quickSort(nums, 0, len(nums) - 1)
        return nums
        
    
    def quickSort(self, nums, s, e):
        if s <= e:
            p = self.partition(nums, s, e)
            self.quickSort(nums, s, p - 1)
            self.quickSort(nums, p + 1, e)
            
            
    def partition(self, nums, s, e):
        pivot = nums[s]
        l = s
        s += 1
        
        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]
            
        while s <= e:
            if nums[s] > pivot and nums[e] < pivot:
                # out of place 
                swap(nums, s, e)
            
            if nums[s] <= pivot:
                s += 1
            if nums[e] >= pivot:
                e -= 1
        swap(nums, l, e)
        return e
        

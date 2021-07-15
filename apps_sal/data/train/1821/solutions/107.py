class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge_sort(nums):
            
            if len(nums) <=1:
                return nums
            
            pivot = int(len(nums)/2)
            
            left = merge_sort(nums[:pivot])
            right = merge_sort(nums[pivot:])
            
            return merge(left, right)
        
        def merge(left, right):
            out = []
            
            left_cursor = 0
            right_cursor = 0
            
            while left_cursor < len(left) and right_cursor < len(right):
                if left[left_cursor] <= right[right_cursor]:
                    out.append(left[left_cursor])
                    left_cursor+=1
                else:
                    out.append(right[right_cursor])
                    right_cursor+=1
            
            out.extend(right[right_cursor:])
            out.extend(left[left_cursor:])
            return out
        
        
        
        
        
        return merge_sort(nums)
        
                    
            


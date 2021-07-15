class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        if len(nums)>1: 
            mid = (len(nums)-1) //2
            left= nums[0:mid+1]
            right = nums[mid+1:]
            left = self.sortArray(left)
            right = self.sortArray(right)
            
            l=r=curr =0
            
            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    nums[curr] = left[l]
                    l +=1
                else:
                    nums[curr] = right[r]
                    r+=1
                curr+=1
                
            while l < len(left):
                nums[curr] = left[l]
                l +=1
                curr+=1
                
            while r < len(right):
                nums[curr] = right[r]
                r+=1
                curr+=1
                
        
        
        return nums


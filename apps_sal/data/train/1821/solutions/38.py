class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return nums
        if len(nums)>1:
            mid=len(nums)//2
            left=nums[:mid]
            right=nums[mid:]
            self.sortArray(left)
            self.sortArray(right)
            self.merge(left,right,nums)
            return nums
    
    def merge(self,left,right,nums):
        i=0
        j=0
        k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                nums[k]=left[i]
                i+=1
                k+=1
            else:
                nums[k]=right[j]
                j+=1
                k+=1
        while i<len(left):
            nums[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            nums[k]=right[j]
            j+=1
            k+=1
        return

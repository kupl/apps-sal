class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)>1: 
            m = len(nums)//2
            left = nums[:m] 
            right = nums[m:] 
            left = self.sortArray(left) 
            right = self.sortArray(right) 
            nums =[] 
            while len(left)>0 and len(right)>0: 
                if left[0]<right[0]: 
                    nums.append(left[0]) 
                    left.pop(0) 
                else: 
                    nums.append(right[0]) 
                    right.pop(0) 

            for i in left:
                nums.append(i) 
            for i in right: 
                nums.append(i) 

        return nums

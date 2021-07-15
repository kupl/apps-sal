class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        nums = self.merge(nums)
        return nums
    
    def merge(self, values):
        if len(values)>1: 
            m = len(values)//2
            left = values[:m] 
            right = values[m:] 
            left = self.merge(left) 
            right = self.merge(right) 

            values =[] 

            while len(left)>0 and len(right)>0: 
                if left[0]<right[0]: 
                    values.append(left[0]) 
                    left.pop(0) 
                else: 
                    values.append(right[0]) 
                    right.pop(0) 

            for i in left: 
                values.append(i) 
            for i in right: 
                values.append(i) 
                  
        return values 
        


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        mid = len(nums)//2
        A = self.sortArray(nums[:mid])
        B = self.sortArray(nums[mid:])
        i,j = 0,0
        result = []
        
        while i < len(A) and j < len(B):
            if A[i] <= B[j]:
                result.append(A[i])
                i += 1
            else:
                result.append(B[j])
                j += 1
                
        if i < len(A):
            result += A[i:]
        elif j < len(B):
            result += B[j:]
            
        return result
        
        


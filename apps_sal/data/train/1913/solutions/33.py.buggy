class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        n = len(A)
        if n<=1: return A
        
        # moving left pointer
        left = n-2
        while left>=0 and A[left]<=A[left+1]: 
            left -= 1
        if left < 0: return A
        
        # moving right pointer, skip same item
        right = n-1
        while A[right]>=A[left]: right -= 1
        while A[right]==A[right-1]: right -= 1
            
        # swap left and right
        A[left],A[right] = A[right],A[left]
        
        return A
        \"\"\"
        i1, n = -1, len(A)
        idx = n-2
        while idx >= 0:
            if A[idx] > A[idx+1]:
                i1 = idx
            else:
                idx -= 1
        
        if i1 == -1:
            return A
        
        # right #
        i2 = n-1
        while A[i2] >= A[i1]:
            i2 -= 1
        while A[i2] == A[i2-1]:
            i2 -= 1
        
        A[i1], A[i2] = A[i2], A[i1]
        return A
        
        
        i1 = -1
        idx = len(nums)-1
        while idx > 0:
            if nums[idx-1] > nums[idx]:
                i1 = idx-1
                break
            else:
                idx -= 1
        
        if i1 == -1:
            return nums
        
        for idx in reversed(range(i1+1, len(nums))):
            if nums[idx] < nums[i1] and nums[idx] != nums[idx-1]:
                nums[i1], nums[idx] = nums[idx], nums[i1]
         
        return nums
        \"\"\"

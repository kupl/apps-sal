class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(nums):
            
            if len(nums)<2:
                return nums
            
            ln = merge(nums[:len(nums)//2])
            rn = merge(nums[len(nums)//2:])
            
            i,j,r = 0, 0, []
            while i<len(ln) or j<len(rn):
                if j<len(rn) and (i==len(ln) or rn[j] < ln[i]):
                    r.append(rn[j])
                    j += 1
                else:
                    r.append(ln[i])
                    i += 1
            return r
        
        return merge(nums)


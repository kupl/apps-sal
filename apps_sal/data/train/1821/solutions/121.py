import math

class Solution:
    
    def merger(self, left, right):
        
        lidx  = 0
        ridx  = 0
        final = []
        
        while lidx < len(left) or ridx < len(right):
            if ridx == len(right):
                final.append(left[lidx])
                lidx += 1
            elif lidx == len(left):
                final.append(right[ridx])
                ridx += 1
            else:
                curt_l = left[lidx]
                curt_r = right[ridx]
                if curt_l <= curt_r:
                    final.append(curt_l)
                    lidx += 1
                else:
                    final.append(curt_r)
                    ridx += 1
        return final


    
    def sortArray(self, nums: List[int]) -> List[int]:
        
        if len(nums) == 1:
            return nums
        elif len(nums) > 1:
            mid_idx = math.ceil(len(nums)/2)
            end_idx = len(nums)
            
            sorted_left  = self.sortArray(nums[0:mid_idx])
            sorted_right = self.sortArray(nums[mid_idx:end_idx])
            
            final = self.merger(sorted_left, sorted_right)
            return final

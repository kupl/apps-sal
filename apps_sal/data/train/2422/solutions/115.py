class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0
        max_val=i_value=y_value = 0
        for i_idx, i_val in enumerate(nums):
            for y_idx, y_val in enumerate(nums):
                if i_idx == y_idx:
                    continue
                if i_val * y_val > max_val : 
                    max_val = i_val * y_val
                    i_value,y_value=i_val,y_val
        return (i_value-1)*(y_value-1)
            


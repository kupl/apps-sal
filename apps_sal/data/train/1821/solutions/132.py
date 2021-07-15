class Solution:
    def merge(self, left, right):
        sorted_list = []
        while left and right:
            if left[0] <= right[0]:
                sorted_list.append(left.pop(0))
            else:
                sorted_list.append(right.pop(0))
        if not left:
            sorted_list+=right
        if not right:
            sorted_list+=left
        return sorted_list
    
                
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<2:
            return nums
        
        mid = len(nums)//2
        
        left = self.sortArray(nums[mid:])
        right = self.sortArray(nums[:mid])

        result = []
        result += self.merge(left, right)
        
        return result
    
    
        \"\"\"Quick sort\"\"\"
#             if len(nums) <= 1:
#                 return nums

#             pivot = random.choice(nums)
#             lt = [v for v in nums if v < pivot]
#             eq = [v for v in nums if v == pivot]
#             gt = [v for v in nums if v > pivot]

#             return self.sortArray(lt) + eq + self.sortArray(gt)

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # merge sort
        if nums == [] or len(nums) == 1:
            return nums
        m = len(nums) // 2
        left = self.sortArray(nums[:m])
        right = self.sortArray(nums[m:])
        
        # merge
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k+= 1
        
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
        
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        
        return nums
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# \t\t# merge sort. If length <= 1, return
# \t\tif not nums or len(nums) <= 1:
# \t\t\treturn nums

# \t\tmid = len(nums) // 2
# \t\tlower = self.sortArray(nums[:mid]) # Lower after sorting
# \t\thigher = self.sortArray(nums[mid:len(nums)]) # Higher after sorting
# \t\tprint(lower, higher)

# \t\ti = j = k = 0
# \t\twhile i < len(lower) and j < len(higher):
# \t\t\tif lower[i] <= higher[j]:
# \t\t\t\tnums[k] = lower[i]
# \t\t\t\ti += 1
# \t\t\telse:
# \t\t\t\tnums[k] = higher[j]
# \t\t\t\tj += 1
# \t\t\tk += 1

# \t\twhile i < len(lower):
# \t\t\tnums[k] = lower[i]
# \t\t\ti += 1
# \t\t\tk += 1
# \t\twhile j < len(higher):
# \t\t\tnums[k] = higher[j]
# \t\t\tj += 1
# \t\t\tk += 1

# \t\treturn nums


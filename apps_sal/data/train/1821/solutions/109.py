class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        if nums == [] or len(nums) == 1:
            return nums
        m = len(nums) // 2
        left = self.sortArray(nums[:m])
        right = self.sortArray(nums[m:])
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        return nums

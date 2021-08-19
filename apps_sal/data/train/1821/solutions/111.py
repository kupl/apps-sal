class Solution:

    def merge(self, num: List[int], nums: List[int], arr: List[int]) -> List[int]:
        i = j = k = 0
        while i < len(num) and j < len(nums):
            if num[i] < nums[j]:
                arr[k] = num[i]
                i += 1
            elif num[i] >= nums[j]:
                arr[k] = nums[j]
                j += 1
            k += 1
        while i < len(num):
            arr[k] = num[i]
            i += 1
            k += 1
        while j < len(nums):
            arr[k] = nums[j]
            j += 1
            k += 1
        return arr

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) != 1:
            mid = len(nums) // 2
            left = self.sortArray(nums[:mid])
            right = self.sortArray(nums[mid:])
            nums = self.merge(left, right, nums)
        return nums

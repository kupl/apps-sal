class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        pivot = len(nums) // 2
        left_arr = self.sortArray(nums[:pivot])
        right_arr = self.sortArray(nums[pivot:])
        return self.merge(left_arr, right_arr)

    def merge(self, left_nums, right_nums):
        (m, n) = (len(left_nums), len(right_nums))
        (i, j) = (0, 0)
        combined_arr = []
        while i < m and j < n:
            if left_nums[i] < right_nums[j]:
                combined_arr.append(left_nums[i])
                i += 1
            else:
                combined_arr.append(right_nums[j])
                j += 1
        combined_arr.extend(left_nums[i:])
        combined_arr.extend(right_nums[j:])
        return combined_arr

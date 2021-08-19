class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        temp = list(range(len(nums)))
        self.helper(nums, 0, len(nums) - 1, temp)
        return nums

    def helper(self, nums, start, end, temp):
        if start >= end:
            return
        mid = (start + end) // 2
        self.helper(nums, start, mid, temp)
        self.helper(nums, mid + 1, end, temp)
        self.merge(nums, start, end, temp)

    def merge(self, nums, start, end, temp):
        mid = (start + end) // 2
        left = start
        right = mid + 1
        temp_index = start
        while left <= mid and right <= end:
            if nums[left] < nums[right]:
                temp[temp_index] = nums[left]
                left += 1
                temp_index += 1
            else:
                temp[temp_index] = nums[right]
                right += 1
                temp_index += 1
        while left <= mid:
            temp[temp_index] = nums[left]
            left += 1
            temp_index += 1
        while right <= end:
            temp[temp_index] = nums[right]
            right += 1
            temp_index += 1
        nums[start:end + 1] = temp[start:end + 1]

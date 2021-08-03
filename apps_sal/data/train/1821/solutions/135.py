class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        tmp = [0 for _ in range(len(nums))]
        self.ms(nums, 0, len(nums) - 1, tmp)
        return nums

    def ms(self, nums, start, end, tmp):
        if start >= end:
            return

        mid = (start + end) // 2
        self.ms(nums, start, mid, tmp)
        self.ms(nums, mid + 1, end, tmp)
        self.merge(nums, start, mid, end, tmp)

    def merge(self, nums, start, mid, end, tmp):
        left, right = start, mid + 1
        idx = start

        while left <= mid and right <= end:
            if nums[left] < nums[right]:
                tmp[idx] = nums[left]
                left += 1
            else:
                tmp[idx] = nums[right]
                right += 1
            idx += 1

        while left <= mid:
            tmp[idx] = nums[left]
            idx += 1
            left += 1

        while right <= end:
            tmp[idx] = nums[right]
            idx += 1
            right += 1

        for i in range(start, end + 1):
            nums[i] = tmp[i]

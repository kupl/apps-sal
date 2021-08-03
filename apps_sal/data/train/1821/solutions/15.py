class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Heap Sort
        # Step 1:
        for i in range(len(nums) // 2, 0, -1):
            self.heapify(nums, i, len(nums) + 1)
        # Step 2:
        for i in range(len(nums), 0, -1):
            index = i - 1
            nums[0], nums[index] = nums[index], nums[0]
            self.heapify(nums, 1, i)

        return nums

    def heapify(self, nums: List[int], index, length):
        left = index * 2
        right = left + 1

        if left >= length:
            return

        if right >= length:
            if (nums[index - 1] < nums[left - 1]):
                nums[index - 1], nums[left - 1] = nums[left - 1], nums[index - 1]
                self.heapify(nums, left, length)
            return

        if nums[left - 1] < nums[right - 1]:
            if (nums[index - 1] < nums[right - 1]):
                nums[index - 1], nums[right - 1] = nums[right - 1], nums[index - 1]
                self.heapify(nums, right, length)
        else:
            if (nums[index - 1] < nums[left - 1]):
                nums[index - 1], nums[left - 1] = nums[left - 1], nums[index - 1]
                self.heapify(nums, left, length)

class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        n = len(nums)
        left = self.sortArray(nums[:n // 2])
        right = self.sortArray(nums[n // 2:])
        n_left = len(left)
        n_right = len(right)
        combine = []
        while n_left > 0 or n_right > 0:
            if n_left and n_right:
                if left[0] > right[0]:
                    combine.append(right.pop(0))
                    n_right -= 1
                else:
                    combine.append(left.pop(0))
                    n_left -= 1
            elif n_left and (not n_right):
                combine += left
                n_left = 0
            elif n_right and (not n_left):
                combine += right
                n_right = 0
        return combine

import math


class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:

        def sort(start, stop):
            if start >= stop:
                return nums[start:stop + 1]
            mid = math.floor((start + stop) / 2)
            left = sort(start, mid)
            right = sort(mid + 1, stop)
            return merge(left, right)

        def merge(left, right):
            left_index = 0
            right_index = 0
            result = []
            while left_index < len(left) and right_index < len(right):
                left_val = left[left_index]
                right_val = right[right_index]
                if left_val < right_val:
                    left_index += 1
                    result.append(left_val)
                else:
                    right_index += 1
                    result.append(right_val)
            if left_index >= len(left):
                result.extend(right[right_index:])
            else:
                result.extend(left[left_index:])
            return result
        return sort(0, len(nums) - 1)

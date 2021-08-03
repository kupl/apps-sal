class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left_array, right_array):
            if not left_array:
                return right_array

            if not right_array:
                return left_array

            left_low = 0
            right_low = 0
            output = []
            while left_low < len(left_array) or right_low < len(right_array):
                if left_low < len(left_array) and right_low < len(right_array):
                    if left_array[left_low] < right_array[right_low]:
                        output.append(left_array[left_low])
                        left_low += 1
                    else:
                        output.append(right_array[right_low])
                        right_low += 1
                elif left_low < len(left_array):
                    output.append(left_array[left_low])
                    left_low += 1
                else:
                    output.append(right_array[right_low])
                    right_low += 1

            return output

        def sort(low, high):
            if low == high:
                return [nums[low]]
            elif low > high:
                return []

            mid = low + (high - low) // 2

            left = sort(low, mid)
            right = sort(mid + 1, high)

            return merge(left, right)

        if not nums:
            return []

        return sort(0, len(nums) - 1)

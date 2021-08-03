class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        pivot = len(nums) // 2
        left_list = self.sortArray(nums[:pivot])
        right_list = self.sortArray(nums[pivot:])
        return self.merge_sort(left_list, right_list)

    def merge_sort(self, left_list, right_list):
        sorted_list = []
        left_idx, right_idx = 0, 0
        while left_idx <= len(left_list) - 1 and right_idx <= len(right_list) - 1:
            if left_list[left_idx] > right_list[right_idx]:
                sorted_list.append(right_list[right_idx])
                right_idx += 1
            else:
                sorted_list.append(left_list[left_idx])
                left_idx += 1

        sorted_list += left_list[left_idx:]
        sorted_list += right_list[right_idx:]

        return sorted_list

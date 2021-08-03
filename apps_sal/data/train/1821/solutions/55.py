class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(left, right):
            res = []
            left_p = right_p = 0
            while left_p < len(left) and right_p < len(right):
                if left[left_p] < right[right_p]:
                    res.append(left[left_p])
                    left_p += 1
                else:
                    res.append(right[right_p])
                    right_p += 1
            res.extend(left[left_p:])
            res.extend(right[right_p:])
            return res

        if len(nums) <= 1:
            return nums
        middle = len(nums) // 2
        left = self.sortArray(nums[:middle])
        right = self.sortArray(nums[middle:])
        if len(left) > len(right):
            return merge_sort(right, left)
        else:
            return merge_sort(left, right)

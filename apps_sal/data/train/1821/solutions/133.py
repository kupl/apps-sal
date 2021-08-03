class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        result = []
        p1 = p2 = 0
        while p1 < len(left) and p2 < len(right):
            if left[p1] < right[p2]:
                result.append(left[p1])
                p1 += 1
            else:
                result.append(right[p2])
                p2 += 1

        result.extend(left[p1:])
        result.extend(right[p2:])

        return result

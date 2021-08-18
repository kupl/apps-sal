class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        L = len(nums)
        if L == 1:
            return nums
        else:
            left = nums[:L // 2]
            right = nums[L // 2:]
            return self.compare(self.sortArray(left), self.sortArray(right))

    def compare(self, left, right):
        combined = []
        while len(left) > 0 and len(right) > 0:
            if left[0] > right[0]:
                combined.append(right.pop(0))
            elif left[0] < right[0]:
                combined.append(left.pop(0))
            else:
                combined.append(right.pop(0))
                combined.append(left.pop(0))
        combined.extend(left)
        combined.extend(right)
        return combined

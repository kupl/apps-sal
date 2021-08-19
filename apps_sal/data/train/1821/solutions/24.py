class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        L = len(nums)
        if L == 1:
            # print(f'nums: {nums}')
            return nums
        else:
            left = nums[:L // 2]
            right = nums[L // 2:]
            # print(left, \"  \", right)
            return self.compare(self.sortArray(left), self.sortArray(right))

    def compare(self, left, right):
        combined = []
        # print(f'before sort: {left}  {right}   {combined}')
        while len(left) > 0 and len(right) > 0:
            if left[0] > right[0]:
                combined.append(right.pop(0))
            elif left[0] < right[0]:
                combined.append(left.pop(0))
            else:  # equal values, pop both to save an iteration.
                combined.append(right.pop(0))
                combined.append(left.pop(0))
        combined.extend(left)  # one will be empty, doesn't matter which
        combined.extend(right)  # one will be empty, doesn't matter which
        # print(f'after sort: {left}  {right}   {combined}')
        return combined

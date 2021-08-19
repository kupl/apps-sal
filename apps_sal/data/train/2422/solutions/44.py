class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        min_val = None
        max_val = None
        for (i, val) in enumerate(nums):
            if min_val is None or min_val[1] > val:
                min_val = [i, val]
            if max_val is None or max_val[1] < val:
                max_val = [i, val]
        answer = 0
        for (i, val) in enumerate(nums):
            if i != min_val[0]:
                answer = max(answer, (min_val[1] - 1) * (val - 1))
            if i != max_val[0]:
                answer = max(answer, (max_val[1] - 1) * (val - 1))
        return answer
